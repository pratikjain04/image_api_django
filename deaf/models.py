from django.db import models


class ImageUploadModel(models.Model):
    image = models.ImageField('images/', null=False, default="")


class ImageModel(models.Model):
    image_url = models.URLField()

    def __str__(self):
        return self.image_url
