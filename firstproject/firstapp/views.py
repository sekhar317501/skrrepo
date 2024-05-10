from django.shortcuts import render
from django.http import HttpResponse

"""def display(request):
    s="<h1> Welcome to Django</h1>"
    return HttpResponse(s)"""
def wish1(request):
    return HttpResponse("<h1> Hello This is from first Application</h1>")

def wish2(request):
    return HttpResponse("<h1> Hello this is from second Apllication </h1>")