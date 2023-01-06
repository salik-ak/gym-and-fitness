from django.urls import path, include
from . import views


urlpatterns = [

    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='updatedata'),


]
