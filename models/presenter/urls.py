from django.conf.urls import url

from models.presenter.views import presenter_view

urlpatterns = [
    url(r'^$', presenter_view, name='presenter'),
]
