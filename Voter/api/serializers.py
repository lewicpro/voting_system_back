from rest_framework import serializers
from ..models import *
from django.contrib.auth import get_user_model
from rest_framework.serializers import CharField, EmailField, ValidationError, SerializerMethodField
from django.db.models import Q
User = get_user_model()



class VotersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voters
        fields=['pk','generated_id', 'voted_for', 'category']
