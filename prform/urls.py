from django.urls import include, path
from prform.views import *

urlpatterns = [
    #path('', include(router.urls)),
    path('first-form', get_name),
    #path('uuids', GetProfileUUIDView.as_view()),
]

#urlpatterns += router.urls
