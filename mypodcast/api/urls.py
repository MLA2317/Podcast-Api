from django.urls import path
from .views import CategoryListCreateApi, CategoryRUDApi, TagListCreateApi,\
    EpisodeListCreateApi, EpisodeRUDApi, CommentListCreate, LikeListApi, LikePostApiView,\
    PlaylistItemCreateAPIView, PlaylistRUDAPIView, PlaylistListCreateAPIView

urlpatterns = [
    # category
    path('cat-list/', CategoryListCreateApi.as_view()),
    path('cat-rud/<int:pk>/', CategoryRUDApi.as_view()),

    # tag
    path('tag-list/', TagListCreateApi.as_view()),

    #like
    path('like-list/', LikeListApi.as_view()),
    path('like-create/<int:episode_id>/', LikePostApiView.as_view()),

    # playlist
    path('playlist-list-create/', PlaylistListCreateAPIView.as_view()),
    path('playlist-rud/<int:pk>/', PlaylistRUDAPIView.as_view()),

    # episode
    path('eps-list/', EpisodeListCreateApi.as_view()),
    path('eps-rud/<int:pk>/', EpisodeRUDApi.as_view()),

    # comment
    path('eps/<int:episode_id>/comment-list/', CommentListCreate.as_view())
]