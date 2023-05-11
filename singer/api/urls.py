from django.urls import path
from rest_framework.authtoken import views
from .views import MySingerListCreateAPi

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('my-singer/', MySingerListCreateAPi.as_view())
]
