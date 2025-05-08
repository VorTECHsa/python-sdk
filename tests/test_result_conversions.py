import pandas as pd

from vortexasdk.result_conversions import format_datatypes


def test_format_datatypes():
    # Create a sample DataFrame with different timestamp formats
    data = {
        "date_col_dont_convert": ["2023-10-01", "2023-10-02"],
        "date_col_timestamp": ["2023-10-01", "2023-10-02"],
        "mixed_iso_format_timestamps": [
            "2023-10-03 12:00:00",
            "2024-01-01 01:01:01.000001",
        ],
        "unix_timestamp": [1696156800, 1696243200],
        "int_values": [1, 2],
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
    assert pd.api.types.is_datetime64_any_dtype(
        formatted_df["date_col_timestamp"]
    )
    assert pd.api.types.is_datetime64_any_dtype(
        formatted_df["mixed_iso_format_timestamps"]
    )
    assert pd.api.types.is_datetime64_any_dtype(formatted_df["unix_timestamp"])
