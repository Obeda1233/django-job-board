from django.shortcuts import render

# Create your views here.
def setting_page(request):
  
    return render(request,'setting/setting.html' )
