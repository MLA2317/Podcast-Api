from django.shortcuts import render, redirect, reverse
from .models import Contact, Subscribe
from .forms import ContactForm, SubscribeForm
from mypodcast.views import Episode, Tag


def contact(request):
    episode = Episode.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    form = ContactForm()
    if request.method == "POST":
        if request.user.is_authenticated:
            form = ContactForm(data=request.POST) #agar modelda blank tru null tru qimasa formsisvalid oqimidi
            if form.is_valid():
                obj = form.save(commit=False)
                obj.name = request.user.singer.full_name
                obj.save()
                return redirect('.')
        else:
            form = ContactForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('.')#qaysi stranisiga turgan bolsa osha stranisiga jonatadi
    forms = SubscribeForm(request.POST or None)
    if forms.is_valid():
        forms.save()  # bu email uchun form
    ctx = {
        'form': form,
        'forms': forms,
        'eps': episode,
        'tags': tags,
    }

    return render(request, 'blog/contact.html', ctx)
