from django.urls import path
from .views import login_view, log_out, register

app_name = 'singer'


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', log_out, name='logout'),
    path('register/', register, name='register'),
]


