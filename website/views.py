from django.shortcuts import render

# Create your views here.
 #path('',about_index,name='about'),
 #   path('skills',skills_index,name='skills'),
 #   path('experience',experience_index,name='experience'),
 #   path('education',education_index,name='education'),
 #   path('contact',contact_index,name='contact')
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
  