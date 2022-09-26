from django.urls import path

from login import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('',views.signin, name='signin'),
    path('logout', views.signout, name="signout"),
    path('home',views.home,name='home')
]