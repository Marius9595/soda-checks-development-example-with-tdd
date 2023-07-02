from unittest import TestCase

from assertpy import assert_that
from soda.scan import Scan

from src.CountriesMetrics import CountriesMetrics
from tests.countries_metrics_stub_builder import CountriesMetricsStubBuilder


class TestSodaChecksForMetricsDatasetOfCountries(TestCase):

    def setUp(self) -> None:
        self.scan = Scan()
        self.scan.set_data_source_name("dask")
        self.dataset_identifier = "countries_metrics"
        self.scan.add_variables(
            {
                "dataset_name": self.dataset_identifier,
            }
        )
        path_yml = "checks.yml"
        self.scan.add_sodacl_yaml_file(path_yml)

    def test_should_detect_metric_column_is_not_in_schema(self):
        countries_metrics = CountriesMetricsStubBuilder().add_entry().build()

        self.scan.add_pandas_dataframe(
            dataset_name=self.dataset_identifier,
            pandas_df=countries_metrics.drop(columns=[CountriesMetrics.metric]),
        )
        self.scan.execute()

        assert_that(self.check_failures_of(self.scan)).contains_only("Schema has the required columns")

    def check_failures_of(self, scan: Scan) -> list[str]:
        check_failures = list(map(lambda check: check.name, scan.get_checks_fail()))
        return check_failures

    def test_should_detect_country_column_is_not_in_schema(self):
        countries_metrics = CountriesMetricsStubBuilder().add_entry().build()

        self.scan.add_pandas_dataframe(
            dataset_name=self.dataset_identifier,
            pandas_df=countries_metrics.drop(columns=[CountriesMetrics.country]),
        )
        self.scan.execute()

        assert_that(self.check_failures_of(self.scan)).contains_only("Schema has the required columns")

    def test_should_detect_value_column_is_not_in_schema(self):
        countries_metrics = CountriesMetricsStubBuilder().add_entry().build()

        self.scan.add_pandas_dataframe(
            dataset_name=self.dataset_identifier,
            pandas_df=countries_metrics.drop(columns=[CountriesMetrics.value]),
        )
        self.scan.execute()

        assert_that(self.check_failures_of(self.scan)).contains_only("Schema has the required columns")

    def test_should_detect_unit_column_is_not_in_schema(self):
        countries_metrics = CountriesMetricsStubBuilder().add_entry().build()

        self.scan.add_pandas_dataframe(
            dataset_name=self.dataset_identifier,
            pandas_df=countries_metrics.drop(columns=[CountriesMetrics.unit]),
        )
        self.scan.execute()

        check_failures = self.check_failures_of(self.scan)
        assert_that(check_failures).contains_only("Schema has the required columns")

    def test_should_detect_year_column_is_not_in_schema(self):
        countries_metrics = CountriesMetricsStubBuilder().add_entry().build()

        self.scan.add_pandas_dataframe(
            dataset_name=self.dataset_identifier,
            pandas_df=countries_metrics.drop(columns=[CountriesMetrics.year]),
        )
        self.scan.execute()

        assert_that(self.check_failures_of(self.scan)).contains_only("Schema has the required columns")

    def test_should_allow_just_metrics_calculated(self):
        countries_metrics = (
            CountriesMetricsStubBuilder()
            .add_entry(metric="invalid metric")
            .build()
        )

        self.scan.add_pandas_dataframe(
            dataset_name=self.dataset_identifier,
            pandas_df=countries_metrics,
        )
        self.scan.execute()

        assert_that(self.check_failures_of(self.scan)).contains_only("Dataset has just calculated metrics")

    def test_should_detect_values_of_percentage_metrics_are_greater_than_upper_limit(self):
        countries_metrics = (
            CountriesMetricsStubBuilder()
            .add_entry(metric="unemployment_rate", value=100.1, unit="percentage")
            .build()
        )

        self.scan.add_pandas_dataframe(
            dataset_name=self.dataset_identifier,
            pandas_df=countries_metrics,
        )
        self.scan.execute()

        assert_that(self.check_failures_of(self.scan)).contains_only(
            "Values of percentage metrics are in range"
        )

    def test_should_detect_values_of_percentage_metrics_are_less_than_lower_limit(self):
        countries_metrics = (
            CountriesMetricsStubBuilder()
            .add_entry(metric="unemployment_rate", value=-0.1, unit="percentage")
            .build()
        )

        self.scan.add_pandas_dataframe(
            dataset_name=self.dataset_identifier,
            pandas_df=countries_metrics,
        )
        self.scan.execute()

        assert_that(self.check_failures_of(self.scan)).contains_only(
            "Values of percentage metrics are in range"
        )
