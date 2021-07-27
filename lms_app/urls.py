from django.contrib import admin
from django.urls import path
from lms_app import views

app_name = "base"


urlpatterns = [
    path("",views.index,name='index'),
    path("create_class/", views.create_class, name='create_class'),
    path("create/",views.create,name='create'),
    path("online_class",views.online,name='online_class')
]
