# Generated by Django 3.2.6 on 2021-08-29 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominees', '0012_rename_author_nominees_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='number_of_votes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
