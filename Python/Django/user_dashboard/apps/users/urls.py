from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^new', views.new),
    url(r'^edit', views.new),
    url(r'^show/(?P<name>\d+)/',views.show),
    # url(r'^edit/(?P<id>)\d+/',views.show),
]