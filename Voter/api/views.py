from ..models import *
from .serializers import *
from django.contrib.auth import get_user_model

from datetime import datetime, timedelta
from django.utils import timezone
# from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework import generics
from rest_framework.views import APIView
from nominees.models import *
from rest_framework.permissions import AllowAny, IsAuthenticated

import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import json

class VotersView(APIView):
    	
	queryset = Voters.objects.all()
	permission_classes = [AllowAny]
      
	def get(self, request, format=None):
		idie = self.request.GET.get('id', None)
		category= self.request.GET.get('category', None)
		name= self.request.GET.get('name', None)
	
		if Voters.objects.filter(category=category, generated_id=idie).exists():
			context={'status':'Voted'}
			return Response(context, status=HTTP_200_OK)
		else:
			context={'status':'Not_Voted'}
			Voters.objects.create(category=category, generated_id=idie, voted_for=name)
			return Response(context, status=HTTP_200_OK)
    			
      



class VoteView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = VotersSerializer
	permission_classes = [AllowAny]


	def get_queryset(self):
		
		return Voters.objects.filter().order_by('-pk')


	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = VotersSerializer(data=data)
		# name=self.kwargs['name']
		if serializer.is_valid(raise_exception=True):
			generatedid = serializer.validated_data['generated_id']
			votedfor = serializer.validated_data['voted_for']
			Number=Nominees.objects.get(name=votedfor)

			gogo = Nominees.objects.filter(name=votedfor).update(number_of_votes=Number.number_of_votes+1)
			mon = serializer.save()
			# gogo.save()
			return Response(serializer.validated_data)
      

class VotersidView(generics.CreateAPIView, generics.ListAPIView):
    	# lookup_field = 'pk'
		serializer_class = VotersSerializer
		permission_classes = [AllowAny]

		def get_queryset(self):
			voterid=self.kwargs['voterid']
			return Voters.objects.filter(generated_id=voterid).order_by('-pk')