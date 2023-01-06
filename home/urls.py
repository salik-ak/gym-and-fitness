from django.urls import path,include
from .import views


urlpatterns = [
    
    path('index/', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('admission/', views.admission,name='admission'),
    path('trainers/', views.trainers,name='trainers'),
    path('logout/', views.logout,name='logout'),
    path('course/', views.course,name='course'),
] 
