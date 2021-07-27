from django.contrib import admin
from django.urls import path
from lms_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "base"


urlpatterns = [
    path("",views.index,name='index'),
    path("create_class/", views.create_class, name='create_class'),
    path("create/",views.create,name='create'),
    path("online_class",views.online,name='online_class'),
    path("create_assignment",views.create_assignment,name='create_assignment')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
