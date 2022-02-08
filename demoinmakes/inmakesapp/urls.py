
# from django.contrib import admin

# from django.urls import path,include
from django.urls import path

from . import views

urlpatterns = [

    path('', views.demo, name='demo'),
    # path('add/',views.addition,name='addition')
    path('', views.rob, name='rob'),
]