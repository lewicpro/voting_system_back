from django.contrib import admin
from .models import *

# Register your models here.
class NomineeAdmin(admin.ModelAdmin):
    search_fields = ('date', 'name', 'category', 'author')
    list_display=['date', 'image',  'name', 'number_of_votes', 'author']
    def get_form(self, request, *args, **kwargs):
         form = super(NomineeAdmin, self).get_form(request, *args, **kwargs)
         form.author = request.user
         return form


    
class VoteResultAdmin(admin.ModelAdmin):
    search_fields = ('date', 'name', 'category')
    
    number_of_votes=models.IntegerField(blank=True, null=True)
    list_display=['image', 'date', 'name', 'category',  'number_of_votes']

class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ('date', 'category_name')
    number_of_votes=models.IntegerField(blank=True, null=True)
    list_display=[ 'date', 'image', 'category_name']


    
admin.site.register(Nominees, NomineeAdmin)
admin.site.register(VoteResults, VoteResultAdmin)
admin.site.register(Categories, CategoriesAdmin)