from django.contrib import admin
from .models import *

# Register your models here.
class NomineeAdmin(admin.ModelAdmin):
    search_fields = ('date', 'name', 'category', 'author')
    list_display=['pk', 'name', 'index_arrange', 'date', 'number_of_votes', 'author']
    list_filter =['category']
  
    def get_form(self, request, *args, **kwargs):
         form = super(NomineeAdmin, self).get_form(request, *args, **kwargs)
         form.author = request.user
         return form
    def get_queryset(self, request):
        queryset=super(NomineeAdmin, self).get_queryset(request)
        queryset=queryset.order_by('-number_of_votes')
        return queryset


    
class VoteResultAdmin(admin.ModelAdmin):
    search_fields = ('date', 'name', 'category')
    
    number_of_votes=models.IntegerField(blank=True, null=True)
    list_display=['image', 'date', 'name', 'category',  'number_of_votes']

class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ('date', 'category_name')
    number_of_votes=models.IntegerField(blank=True, null=True)
    list_display=[ 'date', 'index_arrange', 'image', 'category_name']
class DirectorAdmin(admin.ModelAdmin):
    search_fields = ('pk', 'date', 'username', 'name', 'description')
    # number_of_votes=models.IntegerField(blank=True, null=True)
    list_display=[ 'pk', 'date', 'username', 'name', 'description']


    
admin.site.register(Nominees, NomineeAdmin)
admin.site.register(VoteResults, VoteResultAdmin)
admin.site.register(Director,  DirectorAdmin)
admin.site.register(Categories, CategoriesAdmin)