from django.urls import include, path, re_path
from prfilter.views import *


urlpatterns = [
    path('list', product_list)
]

#urlpatterns += router.urls
