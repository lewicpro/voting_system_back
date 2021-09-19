from rest_framework import serializers
from ..models import *
from django.contrib.auth import get_user_model
from rest_framework.serializers import CharField, EmailField, ValidationError, SerializerMethodField
from django.db.models import Q
from django.contrib.auth.models import User
User = get_user_model()



class VoteResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteResults
        fields=['pk','image', 'date', 'name', 'category',  'number_of_votes']
        
class NomineesSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.category_name')
    author = serializers.SerializerMethodField()
    def get_author(self, obj):
        if obj.author != None:
            print(obj.author.username)
            return obj.author.username

    class Meta:
        model = Nominees
        fields=['pk','image', 'date', 'name', 'category', 'author', 'number_of_votes', 'fullname']

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields=['pk', 'date', 'image', 'category_name']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields=['pk', 'date', 'username', 'name', 'description']
