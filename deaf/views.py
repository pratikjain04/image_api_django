import cv2
from keras.models import load_model
from rest_framework import generics
from .models import ImageUploadModel
from .serializer import FileSerializer
from computervision.prediction import Prediction
from django.shortcuts import HttpResponse
from django import http


class FileUploadView(generics.GenericAPIView):
    queryset = ImageUploadModel.objects.all()
    serializer_class = FileSerializer

    def post(self, request):
        response = Prediction.cvModel(self)
        return http.JsonResponse(response, safe=False)


class GetResultAPIView(generics.GenericAPIView):

    def post(self, request):

        if request.method == 'POST':
            data = request.data

            # Extract age from the post request body
            image_url = float(data['image_url'])

            # load the salary predictor
            pred = Prediction.cvModel(image_url)

            # return a simple HTTP Response
            return HttpResponse(pred)

        else:
            return 'Failed to get model'
