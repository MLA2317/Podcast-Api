from django.core.paginator import Paginator
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Episode, Category, Tag, Season, Like
from .forms import CommentForm
from singer.models import Singer
from django.views.decorators.csrf import csrf_exempt


def index(request):
    episode = Episode.objects.order_by('-id')[:6]
    foot = Episode.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    category = Category.objects.all()
    tag = request.GET.get('tag')
    try:
        author_id = request.user.singer.id
    except:
        author_id = None
    my_like_music = Like.objects.filter(author_id=author_id).values_list('episode_id')
    my_like_music_list = [i[0] for i in my_like_music]
    if tag:
        episode = episode.filter(tags__title__exact=tag)
    ctx = {
        'eps': episode,
        'foot': foot,
        'my_like_music_list': my_like_music_list,
        'tags': tags,
        'category': category
    }
    return render(request, 'blog/index.html', ctx)


def post_view(request, pk):
    obj = Episode.objects.get(id=pk)
    obj.views += 1
    obj.save()
    return redirect(reverse('mypodcast:detail', kwargs={'pk': pk}))


def detail(request, pk):
    obj = get_object_or_404(Episode, id=pk)
    form = CommentForm()
    # if request.method == "POST":
    #     if not request.user.is_authenticated:
    #         return redirect(reverse("mypodcast:detail", kwargs={"pk": pk}))
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('singer:login')
        form = CommentForm(request.POST or None)
        if form.is_valid():
            com = form.save(commit=False)
            com.obj = obj
            com.author = request.user.singer
            com.obj_id = obj.id
            com.save()
            return redirect('.')

    episode = Episode.objects.all()[:3]
    category = Category.objects.all()
    tags = Tag.objects.all()
    singer = Singer.objects.all()
    ctx = {
        'eps': episode,
        'epss': obj,
        'category': category,
        'tags': tags,
        'singer': singer,
        'form': form
    }
    return render(request, 'blog/episode.html', ctx)


def episodes(request):
    episode = Episode.objects.all().order_by('-id')
    category = Category.objects.all()
    tags = Tag.objects.all()
    #tag = Tag.objects.all()
    seasons = Season.objects.all()
    cat = request.GET.get('cat')
    seas = request.GET.get('s')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if cat:
        episode = episode.filter(category__title__exact=cat)
    if seas:
        episode = episode.objects.all().filter(season__title__exact=seas)
    if tag:
        episode = episode.filter(tags__title__exact=tag)
    if q:
        episode = episode.filter(title__icontains=q)
    pag = Paginator(episode, 3)
    page = request.GET.get('page')
    objects = pag.get_page(page)
    ctx = {
        'eps': objects,
        'seasons': seasons,
        'tags': tags,
        'tag': tags,
        'cat': category,
    }
    return render(request, 'blog/episodes.html', ctx)


def get_ids_list(request):
    episode = Episode.objects.all().order_by('-id')
    ids_list = [i.id for i in episode]
    return JsonResponse({'ids_list': ids_list})


@csrf_exempt
def like(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "Login !!!!"}, status=401)
    if request.method == 'POST':
        episode_id = int(request.POST.get('episode_id'))
        user_id = request.user.singer.id
        likes = Like.objects.values_list('episode_id', 'author_id')
        print("=====")
        if (episode_id, user_id) in likes:
            Like.objects.get(episode_id=episode_id, author_id=user_id).delete()
            return JsonResponse({"detail": "Un-Liked"})
        Like.objects.create(episode_id=episode_id, author_id=user_id)
        return JsonResponse({"detail": "Liked"})
    return JsonResponse({"detail": "Method not Allowed"}, status=405)


def archive(request, pk):
    episode = Episode.objects.all().order_by('-id')
    category = Category.objects.all()
    tags = Tag.objects.all()
    #tag = Tag.objects.all()
    seasons = Season.objects.all()
    cat = request.GET.get('cat')
    seas = request.GET.get('s')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60 * 24)
        episode = episode.filter(created_date__gte=now)
    if pk == 2:
        now = datetime.now() - timedelta(minutes=60 * 24 * 7)
        episode = episode.filter(created_date__gte=now)
    if pk == 3:
        now = datetime.now() - timedelta(minutes=60 * 24 * 30)
        episode = episode.filter(created_date__gte=now)
    if pk == 4:
        now = datetime.now() - timedelta(minutes=60 * 24 * 360)
        episode = episode.filter(created_date__gte=now)
    if cat:
        episode = episode.filter(category__title__exact=cat)
    if seas:
        episode = episode.objects.all().filter(season__title__exact=seas)
    if tag:
        episode = episode.filter(tags__title__exact=tag)
    if q:
        episode = episode.filter(title__icontains=q)
    pag = Paginator(episode, 3)
    page = request.GET.get('page')
    objects = pag.get_page(page)
    ctx = {
        'archive': objects,
        'seasons': seasons,
        'tags': tags,
        'tag': tags,
        'cat': category,
    }
    return render(request, 'blog/episodes.html', ctx)