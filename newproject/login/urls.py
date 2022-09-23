from django.urls import path

from login import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('login', views.signin, name='signin'),
    path('logout', views.signout, name="signout"),
]