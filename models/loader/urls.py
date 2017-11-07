from django.conf.urls import url

from models.loader.views import loader_view
from models.loader.handler import load_process

urlpatterns = [
    url(r'^$', loader_view, name='loader'),
    url(r'^load_process/$', load_process, name='load_process'),
]
