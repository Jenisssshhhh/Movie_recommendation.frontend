from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def jen(request):
    return render(request,"home.html")
    


    




