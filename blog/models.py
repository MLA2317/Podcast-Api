from django.db import models
from singer.models import Singer


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='blog_image', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='author_comments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    description = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
