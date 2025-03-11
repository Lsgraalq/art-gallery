from django.contrib import admin
from .models import Painting, AbstractUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Artist

# Создаём кастомный UserAdmin для модели Artist
class ArtistAdmin(UserAdmin):
    model = Artist
    # Указываем поля, которые хотим отображать в админке
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']
    
    # Поля для добавления нового пользователя
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_pic')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_pic')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

# Регистрируем модель Artist с кастомным админом
admin.site.register(Artist, ArtistAdmin)

admin.site.register(Painting)

