from django.urls import path
from .views import gallery, painting_detail, home, donation, author_profile
from django.contrib.auth import views as auth_views
from .views import register, profile




urlpatterns = [
    path('gallery', gallery, name='gallery'),  # Главная страница
    path('painting/<slug:slug>/', painting_detail, name='painting_detail'),
    path('', home, name="home" ),
    path('donation', donation, name="donation" ),
    path('author/<int:user_id>/', author_profile, name="author_profile"),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    # path('author/<int:author_id>', author_render, name="author_render" ),
]

