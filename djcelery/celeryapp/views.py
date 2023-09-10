from django.shortcuts import render
from djcelery.celery import add
# Create your views here.

def index(request):
    print("Results: ")
    add.delay(10,20)
    return render(request,"celeryapp/home.html")

def about(request):
    print("Results: ")
    return render(request,"celeryapp/about.html")


def contact(request):
    print("Results: ")
    return render(request,"celeryapp/contact.html")


