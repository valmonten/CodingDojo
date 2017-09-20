from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^show', views.show),
    url(r'^add', views.add),
    url(r'^', views.index),

]