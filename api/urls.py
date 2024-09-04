from django.urls import path
from .views import *


urlpatterns = [
    path('api/conversion-rate', ConversionRateView.as_view(), name="conversion_rate"),
    path('api/status-distribution', StatusBasedCalculatorView.as_view(), name="status-distribution"),
    path('api/category-type-performance', CategoryTypePerformanceView.as_view(), name="category-type-performance"),
    path('api/filtered-aggregation', FilterAggregationView.as_view(), name="category-type-performance")
]
