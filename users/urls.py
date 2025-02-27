from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.login_view, name="login"),
    path("logout",views.logout_view, name="logout"),
    path("signup",views.signup_view, name="signup"),
    path("earings", views.earings, name="earings"),
    path("braclets",views.braclets, name="braclets"),
    path("necklaces", views.necklaces, name="necklaces"),
    path("piercings", views.piercings, name="piercings"),
    path("contact", views.contact, name="contact")

]