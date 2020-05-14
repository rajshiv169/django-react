from rest_framework import serializers
from .models import common

class CommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = common
        fields = ('id', 'name', 'email', 'message')