from django.urls import path
from .views import logout,login,register,dashboard

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
]