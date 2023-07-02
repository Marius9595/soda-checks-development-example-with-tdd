from unittest import TestCase

from assertpy import assert_that
from soda.scan import Scan

from src.CountriesMetrics import CountriesMetrics
from tests.countries_metrics_stub_builder import CountriesMetricsStubBuilder


class TestSodaChecksForMetricsDatasetOfCountries(TestCase):
    def test_should_detect_metric_column_is_not_in_schema(self):
        countries_metrics = CountriesMetricsStubBuilder().add_entry().build()
        scan = Scan()
        scan.set_data_source_name("dask")
        dataset_identifier = "countries_metrics"
        scan.add_variables(
            {
                "dataset_name": dataset_identifier,
            }
        )
        path_yml = "checks.yml"
        scan.add_sodacl_yaml_file(path_yml)


        scan.add_pandas_dataframe(
            dataset_name=dataset_identifier,
            pandas_df=countries_metrics.drop(columns=[CountriesMetrics.metric]),
        )
        scan.execute()

        check_failures = list(map(lambda check: check.name, scan.get_checks_fail()))
        assert_that(check_failures).contains_only("Schema has the required columns")


