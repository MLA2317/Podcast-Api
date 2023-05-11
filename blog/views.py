from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Blog, Tag, Category
from .forms import CommentForm
from mypodcast.models import Episode


def blog(request):
    blogs = Blog.objects.order_by("-id")[:3]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    episodes = Episode.objects.all()[:3]
    q = request.GET.get('q')
    cate = request.GET.get('cate')
    tage = request.GET.get('tage')
    if tage:
        blogs = blogs.filter(tags__title__exact=tage)
    if cate:
        blogs = blogs.filter(category__title_exact=cate)
    if q:
        blogs = blogs.filter(title__icontains=q)
    pag = Paginator(blogs, 2)
    page = request.GET.get('page')
    blo = pag.get_page(page)
    ctx = {
        'objects': blo,
        'tags': tags,
        'category': categories,
        'eps': episodes,
    }
    return render(request, 'blog/blog.html', ctx)


def detail_blog(request, pk):
    blog_detail = get_object_or_404(Blog, id=pk)
    episodes = Episode.objects.all()[:3]
    category = Category.objects.all()
    tags = Tag.objects.all()
    forms = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('singer:login')
        forms = CommentForm(data=request.POST)
        if forms.is_valid():
            com = forms.save(commit=False)
            com.blog = blog_detail
            com.author = request.user.singer
            com.blog.id = blog_detail.id
            com.save()
            return redirect(".")
    ctx = {
        'blog': blog_detail,
        'eps': episodes,
        'cat': category,
        'tags': tags,
        'forms': forms,
    }
    return render(request, 'blog/blogs.html', ctx)
