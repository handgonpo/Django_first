from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"), 
    #127.0.0.1:8000/accounts/signup/
    #127.0.0.1:8000/accounts/login/

    #127.0.0.1:8000/accounts/signup/
]