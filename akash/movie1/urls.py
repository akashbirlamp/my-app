from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^$', views.index),  # views.py ke ander index function def. kiya hai, $= default
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail),
}
