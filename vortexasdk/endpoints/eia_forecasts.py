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
        List of EIA Forecast object matching 'preset'

        # Examples

        Find PADD5 gasoline imports EIA forecasts from January 2019.
        ```python
        >>> from vortexasdk import EIAForecasts
        >>> df = EIAForecasts().search(
                type="padd5-gasoline-imports",
                filter_time_min="2020-01-01T00:00:00.000Z",
                filter_time_max="2020-01-31T00:00:00.000Z"
            ).to_df()
        ```

        returns

        | date                     | forecast_fri     | value | stocks | cover | runs |
        | ------------------------ | ---------------- | ----- | ------ | ----- | ---- |
        | 2019-01-25T00:00:00.000Z | 48.6277718725167 | 0     | 32811  | 28.8  | 89.4 |
        | 2019-01-18T00:00:00.000Z | 29.5812233704497 | 48    | 32426  | 29.8  | 88.7 |
        | 2019-01-11T00:00:00.000Z | 45.5004976086444 | 0     | 31471  | 29    | 91.8 |
        | 2019-01-04T00:00:00.000Z | 0                |       |        |       |      |


        """
        search_params = {
            "preset": preset,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
        }

        return EIAForecastResult(super().search(**search_params))
