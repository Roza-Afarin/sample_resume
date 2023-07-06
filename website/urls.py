from django.contrib import admin
from django.urls import path,include

from website.views import *

app_name = 'website'

urlpatterns = [
    path('',about_index,name='about'),
    path('skills',skills_index,name='skills'),
    path('experience',experience_index,name='experience'),
    path('education',education_index,name='education'),
    path('contact',contact_index,name='contact')
]
