from django.urls import path
from . import views

urlpatterns = [
path('index/',views.index),
path('navs/',views.navs),
path('register/',views.register),
path('addfrom/',views.addregister),
path('loginfrom/',views.loginfrom),
path('login/',views.login),
path('service/',views.service),
path('index_Cleaning/',views.index_Cleaning),
path('index_Eliminate/',views.index_Eliminate),
path('index_Ironing/',views.index_Ironing),
path('index_landscaping/',views.index_landscaping),
path('index_Massage/',views.index_Massage),
path('index_Pool/',views.index_Pool)

]
