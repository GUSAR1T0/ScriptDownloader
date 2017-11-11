from django.conf.urls import url

from project.models.main.views import main_view

urlpatterns = [
    url(r'^$', main_view, name='main'),
]
