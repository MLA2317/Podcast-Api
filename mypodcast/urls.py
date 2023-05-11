from django.urls import path
from .views import index, detail, episodes, get_ids_list, like, post_view, archive


app_name = 'mypodcast'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('detail/views/<int:pk>/', post_view, name='post_view'),
    path('episodes/', episodes, name='episodes'),
    path('episode/archive/<int:pk>/', archive, name='archive'),
    path('ids_list/', get_ids_list, name='get_ids_list'),
    path('like/', like, name='like')
]