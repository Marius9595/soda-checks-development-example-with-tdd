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

        check_failures = list(map(lambda check: check.name, self.scan.get_checks_fail()))
        assert_that(check_failures).contains_only("Schema has the required columns")

    def test_should_detect_country_column_is_not_in_schema(self):
        countries_metrics = CountriesMetricsStubBuilder().add_entry().build()

        self.scan.add_pandas_dataframe(
            dataset_name=self.dataset_identifier,
            pandas_df=countries_metrics.drop(columns=[CountriesMetrics.country]),
        )
        self.scan.execute()

        check_failures = list(map(lambda check: check.name, self.scan.get_checks_fail()))
        assert_that(check_failures).contains_only("Schema has the required columns")

    def test_should_detect_value_column_is_not_in_schema(self):
        countries_metrics = CountriesMetricsStubBuilder().add_entry().build()

        self.scan.add_pandas_dataframe(
            dataset_name=self.dataset_identifier,
            pandas_df=countries_metrics.drop(columns=[CountriesMetrics.value]),
        )
        self.scan.execute()

        check_failures = list(map(lambda check: check.name, self.scan.get_checks_fail()))
        assert_that(check_failures).contains_only("Schema has the required columns")
