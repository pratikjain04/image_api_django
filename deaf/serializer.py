from rest_framework import serializers
from . models import ImageUploadModel

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUploadModel
        fields = "__all__"