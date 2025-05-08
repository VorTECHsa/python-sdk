from datetime import datetime

import pandas as pd
import pytest

from vortexasdk.result_conversions import format_datatypes


def test_format_datatypes_does_not_convert_columns_without_timestamp_suffix():
    data = {
        "date_col_dont_convert": ["2023-10-01", "2023-10-02", "2023-07-01"],
        "int_values": [1, 2, 3],
    }
    df = pd.DataFrame(data, dtype=str)
    df["int_values"] = df["int_values"].astype(int)

    # Call the function to format datatypes
    formatted_df = format_datatypes(df)

    # Check the columns are not converted to datetime
    assert not pd.api.types.is_datetime64_any_dtype(
        formatted_df["date_col_dont_convert"]
    )
    assert not pd.api.types.is_datetime64_any_dtype(formatted_df["int_values"])


@pytest.mark.parametrize(
    "timestamp_series,col_name,expected_result",
    (
        pytest.param(
            pd.Series(["2023-10-01", "2023-10-02", "2023-07-01"], dtype=str),
            "date_col_timestamp",
            pd.Series(
                [
                    datetime(2023, 10, 1),
                    datetime(2023, 10, 2),
                    datetime(2023, 7, 1),
                ]
            ),
            id="dates are parsed",
        ),
        pytest.param(
            pd.Series(
                [
                    "2023-10-03 12:00:00",
                    "2024-01-01 01:01:01.000001",
                    "2025-07-01T00:00:00",
                ],
                dtype=str,
            ),
            "mixed_iso_format_timestamps",
            pd.Series(
                [
                    datetime(2023, 10, 3, 12),
                    datetime(2024, 1, 1, 1, 1, 1, 1),
                    datetime(2025, 7, 1),
                ]
            ),
            id="mixed ISO formats are parsed",
        ),
        pytest.param(
            pd.Series(
                [
                    "2025/01/31",
                    "2025/01/01",
                    "2025/03/01",
                ],
                dtype=str,
            ),
            "custom_fmt_timestamp",
            pd.Series(
                [
                    datetime(2025, 1, 31),
                    datetime(2025, 1, 1),
                    datetime(2025, 3, 1),
                ]
            ),
            id="non ISO formats are parsed",
        ),
        pytest.param(
            pd.Series(
                [
                    1696118400000000000,
                    1696204800000000000,
                    1688169600000000000,
                ],
            ),
            "unix_timestamp",
            pd.Series(
                [
                    datetime(2023, 10, 1),
                    datetime(2023, 10, 2),
                    datetime(2023, 7, 1),
                ]
            ),
            id="timestamps ints are parsed",
        ),
    ),
)
def test_format_datatypes_converts_columns_with_timestamp_suffix(
    timestamp_series: pd.Series, col_name: str, expected_result: pd.Series
):
    # Create a sample DataFrame with different timestamp formats
    df = pd.DataFrame({col_name: timestamp_series})

    # Call the function to format datatypes
    formatted_df = format_datatypes(df)

    # Check if the columns are converted to datetime
    pd.testing.assert_series_equal(
        formatted_df[col_name],
        expected_result,
        check_names=False,
    )
