from datetime import datetime

import pandas as pd

from vortexasdk.result_conversions import format_datatypes


def test_format_datatypes():
    # Create a sample DataFrame with different timestamp formats
    data = {
        "date_col_dont_convert": ["2023-10-01", "2023-10-02", "2023-07-01"],
        "date_col_timestamp": ["2023-10-01", "2023-10-02", "2023-07-01"],
        "mixed_iso_format_timestamps": [
            "2023-10-03 12:00:00",
            "2024-01-01 01:01:01.000001",
            "2025-07-01T00:00:00",
        ],
        "unix_timestamp": [
            1696118400000000000,
            1696204800000000000,
            1688169600000000000,
        ],
        "int_values": [1, 2, 3],
    }
    df = pd.DataFrame(data, dtype=str)
    df["unix_timestamp"] = df["unix_timestamp"].astype(int)
    df["int_values"] = df["int_values"].astype(int)

    # Call the function to format datatypes
    formatted_df = format_datatypes(df)

    # Check if the columns are converted to datetime
    assert not pd.api.types.is_datetime64_any_dtype(
        formatted_df["date_col_dont_convert"]
    )
    assert not pd.api.types.is_datetime64_any_dtype(formatted_df["int_values"])
    pd.testing.assert_series_equal(
        formatted_df["date_col_timestamp"],
        pd.Series(
            [
                datetime(2023, 10, 1),
                datetime(2023, 10, 2),
                datetime(2023, 7, 1),
            ]
        ),
        check_names=False,
    )
    pd.testing.assert_series_equal(
        formatted_df["mixed_iso_format_timestamps"],
        pd.Series(
            [
                datetime(2023, 10, 3, 12),
                datetime(2024, 1, 1, 1, 1, 1, 1),
                datetime(2025, 7, 1),
            ]
        ),
        check_names=False,
    )
    pd.testing.assert_series_equal(
        formatted_df["unix_timestamp"],
        pd.Series(
            [
                datetime(2023, 10, 1),
                datetime(2023, 10, 2),
                datetime(2023, 7, 1),
            ]
        ),
        check_names=False,
    )
