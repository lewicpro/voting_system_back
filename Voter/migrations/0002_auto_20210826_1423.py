# Generated by Django 3.2.6 on 2021-08-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voters',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='voters',
            name='generated_id',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
