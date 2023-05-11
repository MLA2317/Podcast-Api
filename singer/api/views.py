from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializer import MyProfileSerializer
from ..models import Singer, User


class MySingerListCreateAPi(generics.ListCreateAPIView):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({'detail': 'Authentication is required'}, status=status.HTTP_404_NOT_FOUND)
        profile = Singer.objects.filter(author_id=self.request.user.id).first()
        if profile:
            serializer = MyProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)