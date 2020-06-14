from rest_framework import serializers
from . models import ImageUploadModel

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageUploadModel
        fields = '__all__'