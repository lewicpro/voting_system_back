from django.contrib import admin
from .models import *

# Register your models here.
class VotersAdmin(admin.ModelAdmin):
    search_fields = ('generated_id', 'voted_for'
            )
    list_display=['generated_id', 'voted_for']
admin.site.register(Voters, VotersAdmin)