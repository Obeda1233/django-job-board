from django.shortcuts import render

# Create your views here.
def hone_page(request):
  
    return render(request,'home/home.html' )
