import unittest
import pandas as pd
from api.helpers.filter_aggregation import FilterAggregation

class TestFilterAggregation(unittest.TestCase):

    def setUp(self):
        # Mock data
        self.data = pd.DataFrame({
            'customer_id': [1, 1, 2, 2],
            'type': ['CONVERSION', 'CONVERSION', 'CLICK', 'CONVERSION'],
            'revenue': [100, 200, 300, 400],
            'conversions': [10, 20, 30, 40]
        })

        # Create an instance of FilterAggregation with the mock data
        self.filter_aggregation = FilterAggregation(self.data)

    def test_filter_conversion_data(self):
        # Call the filter_conversion_data method
        filtered_data = self.filter_aggregation.filter_conversion_data()

        # Expected result
        expected_result = pd.DataFrame({
            'customer_id': [1, 1, 2],
            'type': ['CONVERSION', 'CONVERSION', 'CONVERSION'],
            'revenue': [100, 200, 400],
            'conversions': [10, 20, 40]
        })


        self.assertListEqual(filtered_data.loc[:, 'customer_id'].values.tolist(),expected_result.loc[:, 'customer_id'].values.tolist())
        self.assertListEqual(filtered_data.loc[:, 'type'].values.tolist(),expected_result.loc[:, 'type'].values.tolist())
        self.assertListEqual(filtered_data.loc[:, 'revenue'].values.tolist(),expected_result.loc[:, 'revenue'].values.tolist())
        self.assertListEqual(filtered_data.loc[:, 'conversions'].values.tolist(),expected_result.loc[:, 'conversions'].values.tolist())


    def test_analyze_revenue_conversions(self):
        # Call the analyze_revenue_conversions method
        result = self.filter_aggregation.analyze_revenue_conversions()

        # Expected result
        expected_result = pd.DataFrame({
            'customer_id': [1, 2],
            'revenue': [150.0, 400.0],
            'conversions': [15.0, 40.0]
        })

        self.assertListEqual(result.loc[:, 'customer_id'].values.tolist(),expected_result.loc[:, 'customer_id'].values.tolist())
        self.assertListEqual(result.loc[:, 'revenue'].values.tolist(),expected_result.loc[:, 'revenue'].values.tolist())
        self.assertListEqual(result.loc[:, 'conversions'].values.tolist(),expected_result.loc[:, 'conversions'].values.tolist())

