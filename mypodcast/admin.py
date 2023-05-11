from django.contrib import admin
from .models import Episode, Tag, Category, Season, Comment, Like, Playlist, PlaylistItem


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_date']
    list_field = ['category', 'tags']
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'episode', 'author', 'created_date']
    date_hierarchy = 'created_date'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'episode', 'author']


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title']


@admin.register(PlaylistItem)
class PlaymusicAdmin(admin.ModelAdmin):
    list_display = ['id', 'playlist', 'episode']


admin.site.register(Season)

