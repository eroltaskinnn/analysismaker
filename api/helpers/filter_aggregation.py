
class FilterAggregation:
    def __init__(self,data):
        self.data = data

    def filter_conversion_data(self):
        return self.data[self.data['type'] == 'CONVERSION']

    def analyze_revenue_conversions(self):
        filtered_data = self.filter_conversion_data()
        return filtered_data.groupby('customer_id')[['revenue', 'conversions']].mean().reset_index()


class FilterAggregationFactory:
    def __init__(self, analysis):
        self.analysis = analysis

    def calculate_revenue_conversion(self):
        reveneu = self.analysis.analyze_revenue_conversions()

        if reveneu is not None:
            return reveneu.to_dict('records')

