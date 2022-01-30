from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework import viewsets
from .serializers import ImageSerializers
from .models import Image



class home(viewsets.ModelViewSet):

    queryset = Image.objects.all()
    serializer_class = ImageSerializers



    def post(self,requset, *args, **kwargs):
        title = requset.data['title']
        cover = requset.data['cover']

        Image.objects.create(title=title, cover=cover)
        return HttpResponse({'msg': 'Cover created'}, status=200)
