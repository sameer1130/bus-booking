from django.db import models
from core.mixins import AbstractTrack
from .utils import get_image_path
import os

# Create your models here.
class Destination(AbstractTrack):
    destination_name = models.CharField(max_length=20)
    description = models.TextField
    included = models.TextField
    not_included = models.TextField
    dates = models.CharField(max_length=20)
    days = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.destination_name}"
    
class Images(AbstractTrack):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_path,max_length=1000)


    @property
    def file_name(self):
        return os.path.basename(self.image.name)
