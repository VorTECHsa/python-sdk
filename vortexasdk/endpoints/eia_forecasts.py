"""EIA Forecasts Endpoint."""

from vortexasdk.endpoints.eia_forecasts_result import EIAForecastResult
from vortexasdk.endpoints.endpoints import EIA_FORECASTS_RESOURCE
from vortexasdk.operations import Search
from vortexasdk.api.shared_types import to_ISODate


class EIAForecasts(Search):
    """EIA forecasts Endpoint."""

    def __init__(self):
        Search.__init__(self, EIA_FORECASTS_RESOURCE)

    def search(
        self,
        preset: str = None,
        filter_time_min: str = False,
        filter_time_max: str = False,
    ) -> EIAForecastResult:
        """
        Find EIA forecasts for a given date preset and date range.

        # Arguments
            preset: the EIA forecasts preset to be returned. Preset can be: 'padd1-gasoline-imports',
            'padd3-gasoline-imports', 'padd5-gasoline-imports', 'us-gasoline-exports', 'padd1-crude-imports',
            'padd3-crude-imports', 'padd5-crude-imports', 'us-crude-exports', 'padd1-diesel-imports',
            'padd3-diesel-imports', 'padd5-diesel-imports', 'us-diesel-exports', 'padd1-jet-imports',
            'padd5-jet-imports', 'us-jet-exports', 'padd1-fueloil-imports', 'padd3-fueloil-imports',
            'padd5-fueloil-imports' or 'us-fueloil-exports'

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

        """
        search_params = {
            "preset": preset,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
        }

        return EIAForecastResult(super().search(**search_params))
