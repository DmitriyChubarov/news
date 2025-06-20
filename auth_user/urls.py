from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #API
    url(r'^register/',views.RegisterView.as_view(), name='register'),
    url(r'^login/',views.LoginView.as_view(), name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(), name='logout'),

    #HTML
    url(r'^login-html/',views.LoginViewHTML, name='login-html'),
    url(r'^register-html/',views.RegisterViewHTML, name='register-html'),
    url(r'',views.MainViewHTMl, name='main-auth-html'),
]
