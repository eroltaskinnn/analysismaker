import pandas as pd

import unittest
from unittest.mock import patch, MagicMock

from api.helpers.file_operation import Analysis


class TestAnalysis(unittest.TestCase):

    def setUp(self):
        self.analysis = Analysis('test.csv')

    @patch('pandas.read_csv')
    def test_read_data(self, mock_read_csv):
        mock_data = pd.DataFrame({
            'column1': [1, 2, 3],
            'column2': [4, 5, 6]
        })
        mock_read_csv.return_value = mock_data
        data = self.analysis.read_data()
        self.assertIsNotNone(data)
        self.assertEqual(data, True)
        self.assertEqual(self.analysis.data.shape[0], 3)
        self.assertEqual(self.analysis.data.shape[1], 2)
