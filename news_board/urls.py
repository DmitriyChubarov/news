from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create-news/',views.NewsViewPOST.as_view(), name='create-news'),
    url(r'^get-news/',views.NewsViewGET.as_view(), name='get-news'),
    url(r'^get-news-html/',views.NewsViewGetHTML, name='get-news-html'),
    url(r'^edit-news/(?P<pk>\d+)/$',views.NewsViewPATCH.as_view(), name='edit-news'),
    url(r'^delete-news/(?P<pk>\d+)/$',views.NewsViewDELETE.as_view(), name='delete-news'),
]
