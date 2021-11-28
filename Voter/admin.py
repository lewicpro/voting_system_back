from django.contrib import admin
from .models import *

# Register your models here.
class VotersAdmin(admin.ModelAdmin):
    search_fields = ('generated_id', 'voted_for', 'category'
            )
    list_display=['created','generated_id', 'voted_for', 'category']
    list_filter =['voted_for']
admin.site.register(Voters, VotersAdmin)