from django.conf.urls import url

from project.models.loader.helper import load_process
from project.models.loader.views import loader_view

urlpatterns = [
    url(r'^$', loader_view, name='loader'),
    url(r'^load_process/$', load_process, name='load_process'),
]
