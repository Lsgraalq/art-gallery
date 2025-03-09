from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Painting(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='photos/',null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Создаем slug на основе title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title