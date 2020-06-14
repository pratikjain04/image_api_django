from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('image', views.FileUploadView)


urlpatterns = [
    path('', include(routers.urls))
]
