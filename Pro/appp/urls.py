from django.contrib import admin
from django.urls import path
from appp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.jen,name= 'home'),
    
]
