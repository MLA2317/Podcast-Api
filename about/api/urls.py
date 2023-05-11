from django.urls import path
from .views import AboutListCreateAPi


urlpatterns = [
    path('about-list/', AboutListCreateAPi.as_view())
]