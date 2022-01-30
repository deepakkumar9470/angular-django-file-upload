from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from .models import Image

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'cover']