from ..models import *
from .serializers import *
from django.contrib.auth import get_user_model

from datetime import datetime, timedelta
from django.utils import timezone
# from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

import os
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import json

class VoteResultView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = VoteResultSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return VoteResults.objects.all().order_by('-pk')

class NomineesView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = NomineesSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return Nominees.objects.all().order_by('-pk')

class NomineesPullView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = NomineesSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		category=self.kwargs['category']
		catename=Categories.objects.get(category_name=category)
		return Nominees.objects.filter(category=catename.pk).order_by('-pk')

    
class CategoriesView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CategoriesSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return Categories.objects.filter().order_by('-pk')

class CategoriesurlView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CategoriesSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		category=self.kwargs['category']
		return Categories.objects.filter(category_name=category).order_by('-pk')