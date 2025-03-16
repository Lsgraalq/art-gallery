from django.shortcuts import render, get_object_or_404
from .models import Painting
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArtistRegisterForm, PaintingForm
from django.core.paginator import Paginator

def gallery(request):
    paintings = Painting.objects.all()  # Получаем все картины
    paginator = Paginator(paintings, 8)  # Показывать 8 картин на странице
    page_number = request.GET.get('page')  # Получаем номер страницы из запроса
    page_obj = paginator.get_page(page_number)  # Получаем объекты для текущей страницы

    return render(request, 'gallery/gallery.html', {"paintings": page_obj})


def painting_detail(request, slug):
    painting = get_object_or_404(Painting, slug=slug)
    return render(request, 'gallery/painting.html', {'painting': painting})

def home(request):
    return render(request,'gallery/home.html')

def donation(request):
    return render(request,'gallery/donation.html')


User = get_user_model()
def author_profile(request, user_id):
    author = get_object_or_404(User, id=user_id)  # Получаем пользователя или выдаем 404
    paintings = Painting.objects.filter(author=author)  # Все картины этого автора
    print(f"Автор: {author.username}, Количество картин: {paintings.count()} вроде нормас харош братуха 52 слава нашим")  # DEBUG
    # return render(request, 'gallery/author_profile.html', {'author': author, 'paintings': paintings})
    return render(request, 'gallery/author_profile.html', {
        'author': author,
        'paintings': paintings,
    })

@login_required
def profile(request):
    paintings = Painting.objects.filter(author=request.user)  # Здесь может быть фильтрация по текущему пользователю
    return render(request, 'gallery/profile.html', {'paintings': paintings})

def register(request):
    if request.method == 'POST':
        form = ArtistRegisterForm(request.POST)
        if form.is_valid():
            artist = form.save()
            login(request, artist)
            return redirect('profile')
    else:
        form = ArtistRegisterForm()
    
    return render(request, 'gallery/register.html', {'form': form})

@login_required
def add_painting(request):
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        if form.is_valid():
            painting = form.save(commit=False)
            painting.author = request.user  # Присваиваем текущего пользователя
            painting.save()
            return redirect('gallery')  # Перенаправление в галерею
    else:
        form = PaintingForm()
    return render(request, 'gallery/add_painting.html', {'form': form})



@login_required
def delete_painting(request, slug):
    painting = get_object_or_404(Painting, slug=slug, author=request.user)
    painting.delete()
    return redirect('profile')  # Возвращает обратно в кабинет



# views.py
from django.shortcuts import render, redirect
from .forms import ArtistProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request):
    # Получаем текущего пользователя
    artist = request.user
    
    # Проверяем, если форма была отправлена
    if request.method == 'POST':
        form = ArtistProfileForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()  # Сохраняем изменения в профиле
            return redirect('profile')  # Перенаправляем на страницу профиля (можно настроить)

    else:
        form = ArtistProfileForm(instance=artist)
    
    return render(request, 'gallery/edit_profile.html', {'form': form})
