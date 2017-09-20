from django.conf.urls import url
from . import views           # This line is new!

print "Blog app urls"

urlpatterns = [
url(r'^$', views.index),
url(r'^new/$', views.new),
]