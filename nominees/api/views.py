from ..models import *
from .serializers import *
from django.contrib.auth import get_user_model

from datetime import datetime, timedelta
from django.utils import timezone
# from .authentication import AUTH_HEADER_TYPES
# from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework import generics
from Voter.models import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

import os
# from .exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import json

class VoteResultView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = VoteResultSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return VoteResults.objects.all().order_by('-pk')
class NomineesApiView(APIView):
	lookup_field = 'pk'
	serializer_class = NomineesSerializer
	permission_classes = [AllowAny]


	def get(self, request, format=None):
    		
		passed = self.request.GET.get('param', None)
		if passed=='all':
				
			giv=Nominees.objects.all().count()
			categories=Categories.objects.all().count()
			voter=Voters.objects.all().count()
			users=User.objects.all().count()
			print('count', giv)
			
			context={
				'nominees':giv,
				'categories':categories,
				'voters':voter,
				'users':users,
			}
		return Response(context, status=HTTP_200_OK)


class NomineesView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = NomineesSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return Nominees.objects.all().order_by('-number_of_votes')

class NomineesPullView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = NomineesSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		category=self.kwargs['category']
		catename=Categories.objects.get(category_name=category)
		return Nominees.objects.filter(category=catename.pk).order_by('index_arrange')

    
class CategoriesView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CategoriesSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		return Categories.objects.all().order_by('index_arrange')


class CategoriesurlView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CategoriesSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		category=self.kwargs['category']
		return Categories.objects.filter(category_name=category).order_by('index_arrange')



class NomineesurlsView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = NomineesSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		category=self.kwargs['category']
		catename=Categories.objects.get(category_name=category)
		return Nominees.objects.filter(category=catename.pk).order_by('index_arrange')
class DirectorurlView(APIView):
	lookup_field = 'pk'
	serializer_class = DirectorSerializer
	permission_classes = [AllowAny]

	def get(self, request, format=None):
		username = self.request.GET.get('username', None)
		passed = Director.objects.get(username=username)
		context={
			'username':passed.username,
		}
		return Response(context, status=HTTP_200_OK)
