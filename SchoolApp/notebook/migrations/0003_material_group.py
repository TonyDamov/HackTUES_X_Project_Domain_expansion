# Generated by Django 5.0.3 on 2024-03-14 09:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0002_material'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='group',
            field=models.ManyToManyField(related_name='materials', to=settings.AUTH_USER_MODEL),
        ),
    ]
