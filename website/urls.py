from django.contrib import admin
from django.urls import path,include

from website.views import *

app_name = 'website'

urlpatterns = [
    path('',about_index,name='about'),
]
