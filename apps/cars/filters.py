from django_filters import rest_framework as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    brand_start = filters.CharFilter(field_name='brand', lookup_expr='isstartswith')
    brand_end = filters.CharFilter(field_name='brand', lookup_expr='endswith')
    brand_contains = filters.CharFilter(field_name='brand', lookup_expr='contains')

    class Meta:
        model = CarModel
        fields = ('price', 'brand')
