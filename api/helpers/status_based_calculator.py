

class StatusBasedCalculator:
    def __init__(self,data):
        self.data = data

    def analyze_revenue_conversions(self):
        return self.data.groupby('status')[['revenue', 'conversions']].sum().reset_index()


class StatusBasedCalculatorFactory:
    def __init__(self, status_calculator):
        self.status_calculator = status_calculator

    def calculate_revenue_conversion(self):
        reveneu = self.status_calculator.analyze_revenue_conversions()
        if reveneu is not None:
            return reveneu.to_dict('records')



import pandas as pd

# Expected result
expected_result = pd.DataFrame({
    'customer_id': [1, 1, 2],
    'type': ['CONVERSION', 'CONVERSION', 'CONVERSION'],
    'revenue': [100, 200, 400],
    'conversions': [10, 20, 40]
})