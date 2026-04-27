from django.urls import path , include
from .import views

app_name='setting'
urlpatterns = [
    
    path('',views.setting_page,name='setting'),
   
 
]
    