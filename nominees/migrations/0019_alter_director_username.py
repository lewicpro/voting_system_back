# Generated by Django 3.2.6 on 2021-09-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominees', '0018_alter_director_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='username',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
