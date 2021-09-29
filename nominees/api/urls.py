"""back_moneyvendor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import  *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name='nominees'
urlpatterns = [
    url('toke_pro/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^votereult/$', VoteResultView.as_view(), name='voter'),
    url(r'^Categories/$', CategoriesView.as_view(), name='Voter'),
    url(r'^Categories_filter/(?P<category>.+)/$', NomineesurlsView.as_view(), name='Category'),
    url(r'^Categoriesurl/(?P<category>.+)/$', CategoriesurlView.as_view(), name='Voter'),
    url(r'^Contests/(?P<category>.+)/$', NomineesPullView.as_view(), name='Voter'),
    url(r'^director/$', DirectorurlView.as_view(), name='director'),
    url(r'^allnominees/$', NomineesView.as_view(), name='Nomenees'),
    url(r'^getallcounts/$', NomineesApiView.as_view(), name='Nomenees'),

]
