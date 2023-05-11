from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializer import CategorySerializer, TagSerializer, BlogGetSerializer, BlogPostSerializer, CommentSerializer
from ..models import Category, Comment, Tag, Blog


class CategoryListCreateApi(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#
# class CategoryRUDApi(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permissions = [permissions.IsAuthenticatedOrReadOnly]
#     lookup_field = 'pk'


class TagCreateApi(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BlogListCreateApi(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    # serializer_class = BlogGetSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BlogGetSerializer
        if self.request.method == 'POST':
            return BlogPostSerializer
        return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class BlogRUDApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    permissions = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BlogGetSerializer
        return BlogPostSerializer


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        blog_id = self.kwargs.get('blog_id')
        if blog_id:
            qs = qs.filter(blog_id=blog_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['blog_id'] = self.kwargs.get('blog_id')
        return ctx
