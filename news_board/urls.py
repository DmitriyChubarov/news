from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create-news/',views.NewsViewPOST.as_view(), name='create-news'),
    url(r'^get-news/',views.NewsViewGET.as_view(), name='get-news'),
]
