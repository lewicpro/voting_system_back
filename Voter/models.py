from django.db import models

# Create your models here.
class Voters(models.Model):
    generated_id=models.CharField(max_length=120, blank=True, null=True)
    category=models.CharField(max_length=120, blank=True, null=True)
    voted_for=models.CharField(max_length=120, blank=True, null=True)
    voted_id=models.IntegerField(blank=True, null=True)


    class Meta:
        verbose_name_plural = "Voters"
