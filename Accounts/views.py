from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from Accounts.forms import CustomUserForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy


def view_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            if "@gmail.com" in username:
                user_by_email = User.objects.filter(email=username).first()
                user = authenticate(request , username=user_by_email , password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    messages.add_message(request , messages.ERROR , "The information has not been entered correctly !!" , extra_tags="error")
            else:
                user = authenticate(request , username=username , password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    messages.add_message(request , messages.ERROR , "The information has not been entered correctly !!" , extra_tags="error")
    else:
        return redirect("/")
    return render(request,"Accounts/login.html")

@login_required(login_url="/Accounts/login")
def view_logout(request):
    logout(request)
    return redirect("/")

def view_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")
            
        form = CustomUserForm()
        context = {"form":form }
        return render(request,"Accounts/signup.html",context)
    else:
        return redirect("/")   