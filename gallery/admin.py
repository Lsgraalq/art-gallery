from django.contrib import admin
from .models import Painting, Artist
from django.contrib.auth.admin import UserAdmin
from .forms import PaintingAdminForm

# Создаём кастомный UserAdmin для модели Artist
class ArtistAdmin(UserAdmin):
    model = Artist
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'can_post']
    list_filter = ['is_staff', 'is_active', 'can_post']
    search_fields = ['username', 'email']
    ordering = ['username']

    fieldsets = (
        (None, {'fields': ('username', 'password')}), 
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_pic')}), 
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'can_post')}),  # Добавляем can_post сюда
        ('Important dates', {'fields': ('last_login', 'date_joined')}), 
    )
    
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}), 
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_pic')}), 
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'can_post')}),  # И тут тоже
    )

    # Переопределяем save_model, чтобы установить дефолтное изображение, если его нет
    def save_model(self, request, obj, form, change):
        if not obj.profile_pic:
            obj.profile_pic = 'photos/no_image.jpg'  # Устанавливаем дефолтное изображение
        super().save_model(request, obj, form, change)

# Регистрируем модель Artist с кастомным админом
admin.site.register(Artist, ArtistAdmin)

# Создаём кастомный админ для модели Painting
class PaintingAdmin(admin.ModelAdmin):
    form = PaintingAdminForm  # Указываем кастомную форму
    list_display = ('title', 'author', 'auction', 'price', 'is_for_sale', 'year_of_creation')  # Отображаемые поля
    list_filter = ('auction', 'is_for_sale')  # Фильтры
    search_fields = ('title', 'author__username')  # Поиск по имени автора и названию картины
    list_editable = ('auction',)  # Возможность редактировать 'auction' прямо в списке картин

    # Опционально: добавление массовых действий
    actions = ['mark_as_auction']

    def mark_as_auction(self, request, queryset):
        queryset.update(auction=True)
    mark_as_auction.short_description = 'Выставить на аукцион'

# Убедимся, что модель уже не была зарегистрирована
try:
    admin.site.unregister(Painting)
except admin.sites.NotRegistered:
    pass

# Регистрируем модель Painting с кастомным админом
admin.site.register(Painting, PaintingAdmin)
