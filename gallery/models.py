from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.db import models

class Artist(AbstractUser):  # Это твоя кастомная модель пользователя
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    can_post = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Painting(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='paintings')
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='photos/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    auction = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    