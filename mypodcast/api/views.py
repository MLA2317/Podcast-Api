from rest_framework import generics, status, permissions, views
from ..models import Episode, Category, Tag, Comment, Playlist, PlaylistItem, Like
from rest_framework.response import Response
from .serializer import EpisodeGetSerializer, EpisodePostSerializer, CommentsSerializer, CatSerializer, TagsSerializer, \
    LikeGetSerializer, LikePOSTSerializer, PlaylistGetSerializer, PlaylistPostSerializer, MiniPlayListItemSerializer, \
    PlaylistItemPOSTSerializer, PlaylistItemGETSerializer
from .permissions import IsOwner, IsOwnerOrReadOnly, IsAdminUserOrReadOnly



class CategoryListCreateApi(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class CategoryRUDApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer
    permissions = [permissions.IsAdminUser]


class TagListCreateApi(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class LikeListApi(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeGetSerializer
    permissions = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        like = super().get_queryset()
        author = self.request.user.singer
        if author:
            like = like.filter(author_id=author)
            return like
        return []

class LikePostApiView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePOSTSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        ctx = super().get_serializer_context
        ctx['episode_id'] = self.kwargs.get('episode_id')
        return ctx

    def create(self, request, *args, **kwargs):
        episode_id = self.kwargs.get('episode_id')
        author_id = request.user.singer.id
        likes = Like.objects.values_list('episode_id', 'author_id')
        if (episode_id, author_id) in likes:
            Like.objects.get(episode_id=episode_id, author_id=author_id).delete()
            return Response("Un-liked")
        instance = Like.objects.create(author_id=author_id, episode_id=episode_id)
        serializer = LikePOSTSerializer(instance)
        return Response(serializer.data)


class PlaylistListCreateAPIView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlaylistGetSerializer
        return PlaylistPostSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        author = self.request.user.singer
        if author:
            qs = qs.filter(author=author)
            return qs
        return []


class PlaylistRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    permission_classes = [IsOwner]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlaylistGetSerializer
        return PlaylistPostSerializer


class PlaylistItemCreateAPIView(generics.CreateAPIView):
    queryset = PlaylistItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        music_id = self.request.data.get('episode')
        playlist_id = self.kwargs.get('playlist_id')
        music = PlaylistItem.objects.filter(episode_id=music_id, playlist_id=playlist_id)
        if music:
            music.delete()
            return Response({'detail': 'Music has successfully removed from playlist'})
        obj = PlaylistItem.objects.create(episode_id=music_id, playlist_id=playlist_id)
        serializer = PlaylistItemGETSerializer(obj)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlaylistItemGETSerializer
        return PlaylistItemPOSTSerializer


class EpisodeListCreateApi(generics.ListCreateAPIView):
    queryset = Episode.objects.all()
    permissions = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EpisodeGetSerializer
        if self.request.method == 'POST':
            return EpisodePostSerializer
        return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class EpisodeRUDApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Episode.objects.all()
    permissions = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EpisodeGetSerializer
        return EpisodePostSerializer


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        episode_id = self.kwargs.get('episode_id')
        if episode_id:
            qs = qs.filter(episode_id=episode_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['episode_id'] = self.kwargs.get('episode_id')
        return ctx

