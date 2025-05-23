from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/',views.RegisterView.as_view(), name='register'),
    url(r'^register-html/',views.RegisterViewHTML, name='register-html'),
    url(r'^login/',views.LoginView.as_view(), name='login'),
    url(r'^login-html/',views.LoginViewHTML, name='login-html'),
]
