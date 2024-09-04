import pandas as pd



class ConversionRateCalculator:
    def __init__(self,data):
        self.data = data
        self.calculate_conversion_rate()

    def calculate_conversion_rate(self):
        if self.data is None:
            return False

        self.data['conversion_rate'] = self.data['conversions'] / self.data['revenue']
        self.conversion_rates = self.data.groupby('customer_id')['conversion_rate'].mean().reset_index()

        return True

    def get_highest_conversion_rate(self):
        if self.conversion_rates is None:
            raise ValueError("Conversion rates are not calculated")
        return self.conversion_rates.loc[self.conversion_rates['conversion_rate'].idxmax()]

    def get_lowest_conversion_rate(self):
        if self.conversion_rates is None:
            raise ValueError("Conversion rates are not calculated")
        return self.conversion_rates.loc[self.conversion_rates['conversion_rate'].idxmin()]


class ConversionRateFactory:
    def __init__(self, calculator):
        self.calculator = calculator

    def calculate_highest_conversion_rate(self):
        highest_rate = self.calculator.get_highest_conversion_rate()
        if highest_rate is not None:
           result =  {"customer_id": highest_rate["customer_id"],
                    "conversion_rate": highest_rate["conversion_rate"]}
           return result

    def calculate_lowest_conversion_rate(self):
        lowest_rate = self.calculator.get_lowest_conversion_rate()
        if lowest_rate is not None:
           result =  {"customer_id": lowest_rate["customer_id"],
                    "conversion_rate": lowest_rate["conversion_rate"]}
           return result