from django.db import models
from django.utils import timezone

# Create your models here.
class Voters(models.Model):
    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True)
    generated_id=models.CharField(max_length=120, blank=True, null=True)
    category=models.CharField(max_length=120, blank=True, null=True)
    voted_for=models.CharField(max_length=120, blank=True, null=True)
    voted_id=models.IntegerField(blank=True, null=True)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Voters, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "Voters"
