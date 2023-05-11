from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render, reverse
from django.contrib.auth import login, logout


def login_view(request):
    if not request.user.is_anonymous:
        return redirect('mypodcast:episodes')
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_path = request.GET.get('next')
            if next_path:
                return redirect(next_path)
            return redirect("mypodcast:index")
    ctx = {
        'form': form
    }
    return render(request, 'profile/login.html', ctx)


def register(request):
    if request.user.is_authenticated:
        return redirect('mypodcast:episodes')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('singer:login')
    print(form.errors)
    ctx = {
        'form': form,
    }
    return render(request, 'profile/register.html', ctx)


def log_out(request):
    if not request.user.is_authenticated:
        return redirect('singer:login')
    if request.method == 'POST':
        logout(request)
        return redirect('mypodcast:index')
    return render(request, 'profile/logout.html')



