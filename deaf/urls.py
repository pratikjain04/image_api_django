from django.urls import path, include
from . import views

urlpatterns = [
    path('image/', views.FileUploadView.as_view(), name='image'),
    path('result/', views.GetResultAPIView.as_view(), name='result')
]
