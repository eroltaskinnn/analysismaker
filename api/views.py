from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.helpers.category_type_performance import CategoryTypePerformance, CategoryTypePerformanceFactory
from api.helpers.conversion_rate_calculator import ConversionRateCalculator, ConversionRateFactory
from api.helpers.file_operation import FileOperation
from api.helpers.filter_aggregation import FilterAggregation, FilterAggregationFactory
from api.helpers.status_based_calculator import StatusBasedCalculatorFactory, StatusBasedCalculator


class ConversionRateView(APIView):
    def get(self, request):
        """
        Handles HTTP GET requests for conversion rate data.

        Returns:
            A Response object containing the highest and lowest conversion rates.
        """

        file_operation = FileOperation("/home/erol/Downloads/mockupinterviewdata.csv")
        data = file_operation.read_data()

        conversion_rate = ConversionRateCalculator(data)

        conversion_factory = ConversionRateFactory(conversion_rate)

        # Get highest and lowest conversion rates
        highest_conversion_rate = conversion_factory.calculate_highest_conversion_rate()
        lowest_conversion_rate = conversion_factory.calculate_lowest_conversion_rate()

        # Create response data
        data = {
            "highest_conversion_rate": highest_conversion_rate,
            "lowest_conversion_rate": lowest_conversion_rate
        }

        return Response(data, status=status.HTTP_200_OK)

class StatusBasedCalculatorView(APIView):
    def get(self, request):
        """
        Handles HTTP GET requests for the StatusBasedCalculatorView.

        Args:
            request: The HTTP request object.

        Returns:
            A Response object containing the result of the revenue conversion calculation.
        """
        file_operation = FileOperation("/home/erol/Downloads/mockupinterviewdata.csv")
        data = file_operation.read_data()

        status_calculator = StatusBasedCalculator(data)
        status_factory = StatusBasedCalculatorFactory(status_calculator)

        result = status_factory.calculate_revenue_conversion()

        # Create response data
        data = {
            "result": result
        }

        return Response(data, status=status.HTTP_200_OK)


class CategoryTypePerformanceView(APIView):
    def get(self, request):
        """
        Handles HTTP GET requests for category type performance data.

        Returns:
            A Response object containing the result of the category type performance calculation.
        """
        file_operation = FileOperation("/home/erol/Downloads/mockupinterviewdata.csv")
        data = file_operation.read_data()

        analysis = CategoryTypePerformance(data)

        factory = CategoryTypePerformanceFactory(analysis)
        data = factory.calculate_get_max_conversions()

        return Response(data, status=status.HTTP_200_OK)


class FilterAggregationView(APIView):
    def get(self, request):
        """
        Handles HTTP GET requests for filter aggregation data.

        Returns:
            A Response object containing the result of the filter aggregation calculation.
        """
        file_operation = FileOperation("/home/erol/Downloads/mockupinterviewdata.csv")
        data = file_operation.read_data()

        analysis = FilterAggregation(data)

        factory = FilterAggregationFactory(analysis)
        data = factory.calculate_revenue_conversion()

        return Response(data, status=status.HTTP_200_OK)

