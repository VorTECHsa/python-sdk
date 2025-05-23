from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import pandas as pd
from pydantic import BaseModel
from typing_extensions import Literal

from vortexasdk.logger import get_logger

logger = get_logger(__name__)


T = TypeVar("T", bound=BaseModel)


def create_list(
    list_of_dicts: List[Dict[str, Any]], output_class: Type[T]
) -> List[T]:
    """Convert each list element into an instance of the output class."""
    logger.debug(f"Converting list of dictionaries to list of {output_class}")

    return [output_class.model_validate(d) for d in list_of_dicts]


def format_datatypes(df: pd.DataFrame) -> pd.DataFrame:
    """Format the relevant columns with sensible datatypes"""
    timestamp_cols = [col for col in df.columns if "timestamp" in col]

    for col in timestamp_cols:
        if df[col].dtype != "object":
            df[col] = pd.to_datetime(df[col])
        else:
            try:
                df[col] = pd.to_datetime(df[col], format="ISO8601")
            except (ValueError, pd.errors.ParserError):
                logger.debug(
                    f"Failed to parse column=[{col}] using ISO8601 format, trying default"
                )
                df[col] = pd.to_datetime(df[col])

    return df


def create_dataframe(
    data: List[Dict[str, Any]],
    logger_description: str,
    columns: Optional[Union[Literal["all"], List[str]]] = "all",
) -> pd.DataFrame:
    """
    :param columns: Columns to be used in the dataframe
    :param default_columns: Default columns to be used if columns is None
    :param data: records that will be present in the dataframe
    :param logger_description: name of the type of record created. Used for logging.
    :return: pd.DataFrame of records with specified columns
    """
    logger.debug(f"Creating DataFrame of {logger_description}")

    if columns == "all" or columns is None:
        df = pd.DataFrame(data=data).fillna("")
    else:
        df = pd.DataFrame(data=data, columns=columns).fillna("")

    return format_datatypes(df)
