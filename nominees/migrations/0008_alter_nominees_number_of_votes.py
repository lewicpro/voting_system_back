# Generated by Django 3.2.6 on 2021-08-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominees', '0007_alter_nominees_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominees',
            name='number_of_votes',
            field=models.IntegerField(default=0),
        ),
    ]
