# Generated by Django 3.2.6 on 2021-08-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nominees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('image', models.FileField(blank=True, max_length=120, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('category', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name_plural': 'Nominees',
            },
        ),
    ]
