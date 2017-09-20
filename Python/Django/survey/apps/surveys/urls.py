from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^surveys/process', views.process, name='process'),
    url(r'^results', views.results),
    url(r'^$', views.index),
    url(r'^back', views.back),
]