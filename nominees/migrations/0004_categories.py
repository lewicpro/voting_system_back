# Generated by Django 3.2.6 on 2021-08-24 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominees', '0003_auto_20210823_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, max_length=120, null=True, upload_to='')),
                ('category_name', models.CharField(blank=True, max_length=120, null=True)),
                ('number_of_votes', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
