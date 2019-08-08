from django.conf.urls import url
from django.urls import path
from Servicios.views import Servicios
from Servicios.views import Servicios2


urlpatterns = [
    url(r'^$', Servicios.as_view()),
    url(r'^(?P<pk>\d+)$', Servicios2.as_view()),
]

"""
    # Urls Servicios2
    re_path()"""
