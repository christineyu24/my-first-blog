#https://tutorial.djangogirls.org/en/django_urls/

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]