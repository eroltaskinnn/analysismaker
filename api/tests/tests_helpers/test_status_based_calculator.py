import unittest
from unittest.mock import Mock
import pandas as pd
from api.helpers.status_based_calculator import StatusBasedCalculator

class TestStatusBasedCalculator(unittest.TestCase):

    def setUp(self):
        # Mock data
        self.data = pd.DataFrame({
            'status': ['A', 'A', 'B', 'B'],
            'revenue': [100, 200, 300, 400],
            'conversions': [10, 20, 30, 40]
        })

        # Create an instance of StatusBasedCalculator with the mock data
        self.status_based_calculator = StatusBasedCalculator(self.data)

    def test_init(self):
        # Test that the data is set correctly in the __init__ method
        self.assertEqual(self.status_based_calculator.data.shape[0], 4)
        self.assertEqual(self.status_based_calculator.data.shape[1], 3)

    def test_analyze_revenue_conversions(self):
        # Expected result
        expected_result = pd.DataFrame({
            'status': ['A', 'B'],
            'revenue': [300, 700],
            'conversions': [30, 70]
        })

        # Call the analyze_revenue_conversions method
        result = self.status_based_calculator.analyze_revenue_conversions()

        # Assert that the result is equal to the expected result
        pd.testing.assert_frame_equal(result, expected_result)
