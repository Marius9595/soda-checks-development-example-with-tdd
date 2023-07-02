import pandas as pd


class CountriesMetricsStubBuilder:
    def __init__(self):
        self._countries_metrics = []

    def add_entry(
        self,
        country="spain",
        metric="gini_index",
        value=0.5,
        unit="-",
        year=2023,
    ) -> pd.DataFrame:
        self._countries_metrics.append(
            {
                "country": country,
                "metric": metric,
                "value": value,
                "unit": unit,
                "year": year,
            }
        )
        return self

    def build(self) -> pd.DataFrame:
        return pd.DataFrame(self._countries_metrics)
