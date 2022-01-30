from email.policy import default
from django.db import models

# Create your models here.


class Image(models.Model):

    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='images')