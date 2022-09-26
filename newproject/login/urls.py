from django.urls import path

from login import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('user_signin',views.signin, name='signin'),
    path('logout', views.signout, name="signout"),
    path('home',views.home,name='home')
]