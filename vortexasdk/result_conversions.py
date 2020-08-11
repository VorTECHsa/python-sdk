from typing import Union, List

from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.logger import get_logger

import pandas as pd

logger = get_logger(__name__)


def create_list(list_of_dicts, output_class: FromDictMixin) -> List:
    """Convert each list element into an instance of the output class."""
    logger.debug(f"Converting list of dictionaries to list of {output_class}")
    return [output_class.from_dict(d) for d in list_of_dicts]


def format_datatypes(df: pd.DataFrame) -> pd.DataFrame:
    """Format the relevant columns with sensible datatypes"""
    timestamp_cols = [col for col in df.columns if "timestamp" in col]

    for col in timestamp_cols:
        df[col] = pd.to_datetime(df[col])

    return df


def create_dataframe(
    columns: Union[None, List[str]],
    default_columns: List[str],
    data: List[dict],
    logger_description: str,
) -> pd.DataFrame:
    """
    :param columns: Columns to be used in the dataframe
    :param default_columns: Default columns to be used if columns is None
    :param data: records that will be present in the dataframe
    :param logger_description: name of the type of record created. Used for logging.
    :return: pd.DataFrame of records with specified columns
    """
    logger.debug(f"Creating DataFrame of {logger_description}")

    if columns is None:
        df = pd.DataFrame(data=data, columns=default_columns)
    elif columns == "all":
        df = pd.DataFrame(data=data)
    else:
        df = pd.DataFrame(data=data, columns=columns)

    return format_datatypes(df)
