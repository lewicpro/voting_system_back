# Generated by Django 3.2.6 on 2021-09-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominees', '0017_alter_director_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
