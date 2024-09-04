import unittest
from unittest.mock import Mock
import pandas as pd
from api.helpers.category_type_performance import CategoryTypePerformance

class TestCategoryTypePerformance(unittest.TestCase):

    def setUp(self):
        # Mock data
        self.data = pd.DataFrame({
            'category': ['A', 'A', 'B', 'B'],
            'type': ['X', 'X', 'Y', 'Y'],
            'revenue': [100, 200, 300, 400],
            'conversions': [10, 20, 30, 40]
        })

        # Create an instance of CategoryTypePerformance with the mock data
        self.category_type_performance = CategoryTypePerformance(self.data)

    def test_init(self):
        # Test that the data is set correctly in the __init__ method
        self.assertEqual(self.category_type_performance.data.shape[0], 4)
        self.assertEqual(self.category_type_performance.data.shape[1], 4)

    def test_analyze_revenue_conversions(self):
        # Expected result
        expected_result = pd.DataFrame({
            'category': ['A', 'B'],
            'type': ['X', 'Y'],
            'revenue': [300, 700],
            'conversions': [30, 70]
        })

        # Call the analyze_revenue_conversions method
        result = self.category_type_performance.analyze_revenue_conversions()

        # Assert that the result is equal to the expected result
        pd.testing.assert_frame_equal(result, expected_result)

    def test_get_max_conversions_row(self):
        # Expected result
        expected_result = pd.Series({
            'category': 'B',
            'type': 'Y',
            'revenue': 700,
            'conversions': 70
        })

        # Call the get_max_conversions_row method
        result = self.category_type_performance.get_max_conversions_row()

        # Assert that the result is equal to the expected result
        self.assertEqual(result["category"], expected_result["category"])
        self.assertEqual(result["type"], expected_result["type"])
        self.assertEqual(result["revenue"], expected_result["revenue"])
        self.assertEqual(result["conversions"], expected_result["conversions"])

if __name__ == '__main__':
    unittest.main()