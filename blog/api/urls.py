from django.urls import path
from .views import CategoryListCreateApi, TagCreateApi, BlogListCreateApi, BlogRUDApi, CommentListCreate


urlpatterns = [
    # path('category-rud/<int:pk>/', CategoryRUDApi.as_view()),
    path('category-list/', CategoryListCreateApi.as_view()),
    path('tag-list/', TagCreateApi.as_view()),
    path('blog-list/', BlogListCreateApi.as_view()),
    path('blog-rud/<int:pk>/', BlogRUDApi.as_view()),
    path('blog/<int:blog_id>/comment/', CommentListCreate.as_view())
]
