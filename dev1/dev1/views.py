from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    # return HttpResponse("Hey candy!!,home")
    return render(req,'index.html')


def about(req):
    return HttpResponse("Hey candy!!, about")


def contact(req):
    return HttpResponse("Hey candy!!,contact")


def help(req):
    return HttpResponse("Hey candy!!, help")
