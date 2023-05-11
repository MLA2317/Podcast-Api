from django.shortcuts import render
from .models import About
from contact.forms import SubscribeForm
from mypodcast.views import Episode, Tag, Like
from blog.models import Blog


def about(request):
    episode = Episode.objects.order_by('-id')[:3]
    mypodcast = Episode.objects.all().count
    blog = Blog.objects.all().count
    like = Like.objects.all().count
    tags = Tag.objects.all()
    forms = SubscribeForm(request.POST or None)
    if forms.is_valid():
        forms.save()
    objects = About.objects.all()
    ctx = {
        'objs': objects,
        'forms': forms,
        'eps': episode,
        'tags': tags,
        'mypodcast_count': mypodcast,
        'blog_count': blog,
        'like_count': like,
    }
    return render(request, 'blog/about.html', ctx)
