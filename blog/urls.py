from django.urls import path
from .views import blog, detail_blog

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('details/<int:pk>/', detail_blog, name='blogs'),
]
