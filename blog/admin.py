from django.contrib import admin
from .models import Blog, Category, Tag, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_date']
    list_field = ['category', 'tag']
    filter_horizontal = ('tag',)
    date_hierarchy = 'created_date'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'author', 'created_date']
    date_hierarchy = 'created_date'
