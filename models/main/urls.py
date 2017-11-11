from django.conf.urls import url

from models.main.views import main

urlpatterns = [
    url(r'^$', main, name='main'),
]
