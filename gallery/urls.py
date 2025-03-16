from django.urls import path
from .views import gallery, painting_detail, home, donation, author_profile, register, profile, add_painting, delete_painting, edit_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('gallery/', gallery, name='gallery'),
    path('painting/<slug:slug>/', painting_detail, name='painting_detail'),
    path('', home, name='home'),
    path('donation/', donation, name='donation'),
    path('author/<int:user_id>/', author_profile, name='author_profile'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='gallery/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='gallery/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),  # Путь для профиля
    path('add_painting/', add_painting, name='add_painting'),
    path('painting/delete/<slug:slug>/', delete_painting, name='delete_painting'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]