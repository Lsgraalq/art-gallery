import os
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from unidecode import unidecode

class Artist(AbstractUser):  # Это твоя кастомная модель пользователя
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/',null=False, blank=False, default='photos/no_image.jpg')
    can_post = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Painting(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='paintings')
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='photos/', null=False, blank=False, default='photos/no_image.jpg')
    slug = models.SlugField(unique=True, blank=True)
    auction = models.BooleanField(default=False)  # Выставлено ли на аукцион
    width = models.FloatField(null=True, blank=True)  # Ширина картины
    height = models.FloatField(null=True, blank=True)  # Высота картины
    paint_type = models.CharField(max_length=100, blank=True)  # Тип краски
    canvas_material = models.CharField(max_length=100, blank=True)  # Материал холста
    is_for_sale = models.BooleanField(default=False)  # Продажа картины или нет
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Цена картины, если она продается
    year_of_creation = models.PositiveIntegerField(null=True, blank=True)  # Год выпуска картины

    from django.db.models import Q

    def save(self, *args, **kwargs):
        if not self.slug:
            # Генерируем базовый слаг из названия
            base_slug = slugify(unidecode(self.title))
            # Проверяем, существует ли уже такой слаг в базе данных
            existing_slug = Painting.objects.filter(slug=base_slug).exists()
            
            # Если слаг существует, добавляем числовой суффикс
            if existing_slug:
                counter = 1
                while Painting.objects.filter(slug=f"{base_slug}-{counter}").exists():
                    counter += 1
                self.slug = f"{base_slug}-{counter}"
            else:
                self.slug = base_slug
        
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        # Удаляем файл изображения перед удалением объекта
        if self.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
            if os.path.exists(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

