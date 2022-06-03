
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *
from graphene_django.views import GraphQLView

urlpatterns = [
    # ...
    path('', home_page, name="home_page"),
    path('thank_you', thank_you, name="thank_you"),

]
