from django.shortcuts import render

# Create your views here.

def about_index(request):
    return render(request,'index.html')

def skills_index(request):
    return render(request,'index.html')

def experience_index(request):
    return render(request,'index.html')

def education_index(request):
    return render(request,'index.html')

def contact_index(request):
    return render(request,'index.html')
  