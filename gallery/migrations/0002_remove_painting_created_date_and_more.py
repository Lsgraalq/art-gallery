# Generated by Django 5.1.7 on 2025-03-07 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='painting',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='painting',
            name='published_date',
        ),
    ]
