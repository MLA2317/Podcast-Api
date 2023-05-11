from rest_framework import serializers
from ..models import Episode, Comment, Category, Tag, Like, Playlist, PlaylistItem


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'image']


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class EpisodeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'title', 'description', 'image', 'song', 'author', 'tags', 'category', 'season', 'views', 'created_date']


class EpisodePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'title', 'description', 'image', 'song', 'author', 'tags', 'category', 'season', 'views', 'created_date']

    def create(self, validated_data):
        request = self.context['request']
        author = request.user.singer
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class LikeGetSerializer(serializers.ModelSerializer):
    episode = EpisodeGetSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['episode']


class LikePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'author', 'episode']
        extra_kwargs = {
            'author': {'required': False},
            'episode': {'required': False},
        }


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'episode', 'name', 'text', 'created_date']

    def create(self, validated_data):
        request = self.context['request']
        episode_id = self.context['episode_id']
        name = self.context['name']
        author_id = request.user.singer.id
        text = self.context['text']
        instance = Comment.objects.create(episode_id=episode_id, name=name, author_id=author_id, text=text)
        return instance



class MiniEpisodeSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.user.username', read_only=True)
    category = serializers.CharField(source='category.title', read_only=True)
    tags = TagsSerializer(read_only=True, many=True)
    season = serializers.CharField(source='season.title', read_only=True)

    class Meta:
        model = Episode
        fields = '__all__'

class MiniPlayListItemSerializer(serializers.ModelSerializer):
    episode = MiniEpisodeSerializer(read_only=True)

    class Meta:
        model = PlaylistItem
        fields = ['id', 'episode']


class PlaylistGetSerializer(serializers.ModelSerializer):
    items = MiniPlayListItemSerializer(read_only=True, many=True)

    class Meta:
        model = Playlist
        fields = ['id', 'author', 'title', 'items']


class PlaylistPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = ['id', 'title', 'author']
        extra_kwargs = {
            'author': {'required': False}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.singer
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class PlaylistItemGETSerializer(serializers.ModelSerializer):
    episode = MiniEpisodeSerializer(read_only=True)
    class Meta:
        model = PlaylistItem
        fields = ['id', 'episode']

class PlaylistItemPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistItem
        fields = ['id', 'playlist', 'episode']





