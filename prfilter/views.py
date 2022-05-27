from django.shortcuts import render
from prfilter.filters import ProductFilter
from prfilter.models import Product

# Create your views here.


def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'product_list.html', {'filter': f})
