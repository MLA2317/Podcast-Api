from django.db import models
from singer.models import Singer
from django.contrib.auth.forms import User


class Category(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    image = models.ImageField(upload_to='media/category')

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title


class Season(models.Model):
    title = models.CharField(max_length=225)
    season_id = models.CharField(max_length=225)


class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/image')
    song = models.FileField(upload_to='media/music', null=True, blank=True)
    author = models.ForeignKey(Singer, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     if self.author.get_full_name() != '':
    #         return f"{self.title} - {self.author.get_full_name}"
    #     return f"{self.title} - {self.author.username}"


class Comment(models.Model):
    author = models.ForeignKey(Singer, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=225, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     if self.author.user.get_full_name():
    #         return f"{self.author.user.get_full_name}'s comment"
    #     return f"{self.author.user.username}'s comment"

    class Meta:
        ordering = ['-id']


class Like(models.Model):
    author = models.ForeignKey(Singer, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)


class Playlist(models.Model):
    author = models.ForeignKey(Singer, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class PlaylistItem(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='items')
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True)
