from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def all_app(req):
    return render(req,'app1/all_app1.html')

def profile(req):
    return HttpResponse("Hi there")