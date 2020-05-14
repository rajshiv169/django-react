from django.shortcuts import render
from .models import common
from.serializers import CommonSerializer
from rest_framework import generics

# Create your views here.
class CommonListCreate(generics.ListCreateAPIView):
    queryset = common.objects.all()
    serializer_class = CommonSerializer
