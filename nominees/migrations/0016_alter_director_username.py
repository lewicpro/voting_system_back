# Generated by Django 3.2.6 on 2021-09-19 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominees', '0015_alter_director_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='username',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
