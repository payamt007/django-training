import django_filters
from prfilter.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='ixact')

    class Meta:
        model = Product
        fields = ['name', 'price']
