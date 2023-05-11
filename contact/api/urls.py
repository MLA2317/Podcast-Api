from django.urls import path
from .views import ContactListCreate, SubscribeListCreate


urlpatterns = [
    path('contact-list/', ContactListCreate.as_view()),
    path('email-list/', SubscribeListCreate.as_view()),
]
