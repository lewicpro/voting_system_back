# Generated by Django 3.2.6 on 2021-08-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominees', '0005_nominees_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='nominees',
            name='is_image_compressed',
            field=models.BooleanField(default=False),
        ),
    ]
