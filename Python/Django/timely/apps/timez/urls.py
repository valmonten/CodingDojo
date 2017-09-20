from django.conf.urls import url
from . import views

print "Blog app urls"

urlpatterns = [
url(r'^', views.index),

]