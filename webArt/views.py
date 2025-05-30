from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib import messages

def view_home(request):
    return render(request, "webArt/index.html")

def view_contact(request):
    return render(request , "webArt/contact.html")
