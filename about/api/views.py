from rest_framework import generics
from .serializer import AboutSerializer
from..models import About


class AboutListCreateAPi(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer