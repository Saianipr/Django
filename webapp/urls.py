from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),

    url(r'^my/',views.first),
    url(r'^contact/',views.contact)
]