import cv2
from keras.models import load_model
from rest_framework import generics
from minor.settings import MEDIA_URL
from .models import ImageUploadModel
from .serializer import FileSerializer
from computervision.prediction import Prediction
from django.shortcuts import HttpResponse

class FileUploadView(generics.GenericAPIView):

    queryset = ImageUploadModel.objects.all()
    serializer_class = FileSerializer

    def post(self, request):
        response = Prediction.cvModel(MEDIA_URL)
        return HttpResponse(response);
