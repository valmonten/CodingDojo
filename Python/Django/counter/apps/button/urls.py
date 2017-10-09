from django.conf.urls import url
import views

urlpatterns = [
    url(r'^go', views.go),
    url(r'^$', views.show),
]