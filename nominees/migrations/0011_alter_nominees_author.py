# Generated by Django 3.2.6 on 2021-08-26 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nominees', '0010_nominees_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominees',
            name='Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]