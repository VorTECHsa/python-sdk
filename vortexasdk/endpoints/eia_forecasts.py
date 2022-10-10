"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Feia_forecasts.ipynb)
"""
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

        response = super().search_with_client(
            exact_term_match=None,
            response_type=None,
            headers=None,
            **search_params
        )

        return EIAForecastResult(
            records=response["data"], reference=response["reference"]
        )
