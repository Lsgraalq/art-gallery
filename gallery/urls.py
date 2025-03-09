from django.urls import path
from . import views
from .views import gallery, painting_detail, home, donation


urlpatterns = [
    path('gallery', gallery, name='gallery'),  # Главная страница
    path('painting/<slug:slug>/', painting_detail, name='painting_detail'),
    path('', home, name="home" ),
    path('donation', donation, name="donation" ),
]