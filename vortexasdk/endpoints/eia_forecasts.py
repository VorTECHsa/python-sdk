"""EIA Forecasts Endpoint."""

from vortexasdk.endpoints.eia_forecasts_result import EIAForecastResult
from vortexasdk.endpoints.endpoints import EIA_FORECASTS_RESOURCE
from vortexasdk.operations import Search
from vortexasdk.api.shared_types import to_ISODate
from datetime import datetime


class EIAForecasts(Search):
    """EIA forecasts Endpoint, use this to search through Vortexa's EIA Forecasts data.

    The data includes:

    - `date`: date of the forecast
    - `forecast_fri`: Vortexa's data science based forecast of the EIA number to be published on the week
    - `value`: Actual EIA import/export numbers as published by the EIA Weekly Supply Estimates report
    - `stocks`: EIA stocks (kbl)
    - `cover`: Cover (days of Supply for the whole of the US, as published by the EIA Weekly Supply Estimates report)
    - `runs`: refinery runs (refiner “Percent Operable Utilization” as published by the EIA Weekly Supply Estimates report)

    """

    def __init__(self):
        Search.__init__(self, EIA_FORECASTS_RESOURCE)

    def search(
        self,
        preset: str = "padd1-gasoline-imports",
        filter_time_min: datetime = datetime(2020, 1, 1),
        filter_time_max: datetime = datetime(2020, 1, 31),
    ) -> EIAForecastResult:
        """
        Find EIA forecasts for a given preset and date range.

        # Arguments
            preset: Use to specify what geography and product information you would like to query.
            Preset can be: 'padd1-gasoline-imports', 'padd3-gasoline-imports', 'padd5-gasoline-imports',
            'us-gasoline-exports', 'padd1-crude-imports', 'padd3-crude-imports', 'padd5-crude-imports',
            'us-crude-exports', 'padd1-diesel-imports', 'padd3-diesel-imports', 'padd5-diesel-imports',
            'us-diesel-exports', 'padd1-jet-imports', 'padd5-jet-imports', 'us-jet-exports',
            'padd1-fueloil-imports', 'padd3-fueloil-imports', 'padd5-fueloil-imports' or 'us-fueloil-exports'

            filter_time_min: The UTC start date of the time filter

            filter_time_max: The UTC end date of the time filter

        # Returns
        List of EIA Forecast object matching selected 'preset'.

        # Examples

        Find PADD5 gasoline imports EIA forecasts from January 2019.
        ```python
        >>> from datetime import datetime
        >>> from vortexasdk import EIAForecasts
        >>> df = EIAForecasts().search(
        ...     preset="padd5-gasoline-imports",
        ...     filter_time_min=datetime(2020, 1, 1),
        ...     filter_time_max=datetime(2020, 1, 31)
        ... ).to_df()

        ```

        returns

        | date                     | forecast_fri     | value | stocks | cover | runs |
        | ------------------------ | ---------------- | ----- | ------ | ----- | ---- |
        | 2020-01-31T00:00:00.000Z | 454.96048964485  | 323   | 9541   | 26.5  | 65.9 |
        | 2020-01-24T00:00:00.000Z | 545.453497230504 | 579   | 10461  | 25.9  | 61.5 |
        | 2020-01-17T00:00:00.000Z | 510.289752707662 | 549   | 10325  | 25.2  | 64.7 |
        | 2020-01-10T00:00:00.000Z | 469.841470826967 |       |        |       |      |
        | 2020-01-03T00:00:00.000Z | 640.443229654771 |       |        |       |      |

        Some values can be NULL: value, stocks, cover, runs. It can happen when:

        - it's a very recent forecast, the Vortexa's data science based forecast (forecast_fri) is available but
          the complete EIA data isn't yet
        - it's an older forecast and the data is not available

        """
        search_params = {
            "preset": preset,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
        }

        return EIAForecastResult(super().search(**search_params))
