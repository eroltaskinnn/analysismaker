import unittest
from unittest.mock import Mock
import pandas as pd
from api.helpers.conversion_rate_calculator import ConversionRateCalculator

class TestConversionRateCalculator(unittest.TestCase):

    def setUp(self):
        # Mock data
        self.data = pd.DataFrame({
            'customer_id': [1, 2, 3, 4],
            'conversions': [10, 20, 30, 40],
            'revenue': [100, 200, 300, 400]
        })

        # Create an instance of ConversionRateCalculator with the mock data
        self.conversion_rate_calculator = ConversionRateCalculator(self.data)

    def test_calculate_conversion_rate(self):
        # Call the calculate_conversion_rate method
        result = self.conversion_rate_calculator.calculate_conversion_rate()

        # Check that the conversion_rate column is added to the data
        self.assertIn('conversion_rate', self.conversion_rate_calculator.data.columns)

        # Check that the conversion_rate values are correct
        expected_conversion_rates = [0.1, 0.1, 0.1, 0.1]
        self.assertEqual(self.conversion_rate_calculator.data['conversion_rate'].tolist(), expected_conversion_rates)

        # Check that the conversion_rates attribute is set correctly
        self.assertIsNotNone(self.conversion_rate_calculator.conversion_rates)

        # Check that the result is True
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()