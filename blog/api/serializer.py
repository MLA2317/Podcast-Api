from rest_framework import serializers
from ..models import Blog, Comment, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class BlogGetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'image', 'category', 'tag', 'description', 'created_date']


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'image', 'category', 'tag', 'description', 'created_date']

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'blog', 'description', 'created_date']

    def create(self, validated_data):
        request = self.context['request']
        blog_id = self.context['blog_id']
        author_id = request.user.singer.id
        description = validated_data.get('description')
        instance = Comment.objects.create(blog_id=blog_id, author_id=author_id, description=description)
        return instance
