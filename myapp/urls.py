from django.urls import path
from .views import *
 
urlpatterns = [
 
    path('', SigninView,name='signin'),
    path('dash/', DashView,name='dash'),
    path('logout/',logoutView,name='logout'),
 
]
