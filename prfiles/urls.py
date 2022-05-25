from django.urls import include, path, re_path
from prfiles.views import *


urlpatterns = [
    # ...
    re_path(r'^upload/(?P<filename>[^/]+)$', UploadHandlerView.as_view())
]

#urlpatterns += router.urls
