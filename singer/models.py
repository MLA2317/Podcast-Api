from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Singer(models.Model):
    PROFESSION = (
        (0, 'Rock'),
        (1, 'Pop'),
        (2, 'Classic'),
        (3, 'Rap'),
        (4, 'Djazz')
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='singer', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profession = models.IntegerField(choices=PROFESSION, null=True, blank=True)

    def __str__(self):
        return self.author.username

    @property
    def full_name(self):
        if self.author.get_full_name():
            return self.author.get_full_name()
        return self.author.username


def user_post_save(instance, sender, created, *args, **kwargs):
    if created:
        Singer.objects.create(author_id=instance.id)


post_save.connect(user_post_save, sender=User)
