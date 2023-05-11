from rest_framework import generics
from .serializer import ContactSerializer, SubscribeSerializer
from ..models import Contact, Subscribe


class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SubscribeListCreate(generics.ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

