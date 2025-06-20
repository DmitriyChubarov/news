from django.conf.urls import url
from . import views

urlpatterns = [
    #HTML

    #API  
    url(r'^create-comment/',views.CommentsViewCreate.as_view(), name='create-comment'),
    url(r'^delete-comment/(?P<pk>\d+)/$',views.CommentsViewDelete.as_view(), name='delete-comment'),
]
