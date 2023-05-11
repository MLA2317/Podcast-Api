from rest_framework import serializers
from ..models import Singer


class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'author', 'image', 'bio']