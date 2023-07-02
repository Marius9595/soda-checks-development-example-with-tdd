import dataclasses


@dataclasses.dataclass(frozen=True)
class CountriesMetrics:
    country = "country"
    metric = "metric"
    value = "value"
    unit = "unit"
    year = "year"

    @property
    def columns(self) -> list[str]:
        return [
            self.country,
            self.metric,
            self.value,
            self.unit,
            self.year,
        ]
