from django.db import models

class ImageUploadModel(models.Model):
    image = models.ImageField('images/', null = False, default="")