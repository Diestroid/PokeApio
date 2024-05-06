from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("wiki/", views.wiki, name="wiki"),
    path("logout/", views.signout, name="signout"),
    path("login/", views.signin, name="signin"),
]
