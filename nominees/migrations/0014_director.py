# Generated by Django 3.2.6 on 2021-09-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominees', '0013_alter_categories_number_of_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=120, null=True)),
                ('username', models.CharField(blank=True, max_length=120, null=True)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=920, null=True)),
            ],
        ),
    ]