

class CategoryTypePerformance:
    def __init__(self,data):
        self.data = data

    def analyze_revenue_conversions(self):
        return self.data.groupby(['category', 'type'])[['revenue', 'conversions']].sum().reset_index()

    def get_max_conversions_row(self):
        return self.analyze_revenue_conversions().loc[self.analyze_revenue_conversions()['conversions'].idxmax()]


class CategoryTypePerformanceFactory:
    def __init__(self, analysis):
        self.analysis = analysis

    def calculate_get_max_conversions(self):

        category_type = self.analysis.get_max_conversions_row()

        if category_type is not None:
            result  = {
                "category": category_type["category"],
                "type": category_type["type"],
                "revenue": category_type["revenue"],
                "conversions": category_type["conversions"]
            }

            return result
