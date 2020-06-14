from rest_framework import viewsets
from . models import ImageUploadModel
from . serializer import FileSerializer
from django.shortcuts import render
from rest_framework import generics

class FileUploadView(viewsets.ModelViewSet):
    queryset = ImageUploadModel.objects.all()
    serializer_class = FileSerializer