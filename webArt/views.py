from django.shortcuts import render , get_object_or_404 , redirect
from Artwork.models import Artwork 
from Artist.models import Post 
from webArt.forms import Contactform
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def view_home(request):
    time_now=timezone.localtime(timezone.now())
    posts = Artwork.objects.filter(poblished_date__lte=time_now , status = 1 )[:3]
    Artists = Post.objects.filter(poblished_date__lte=time_now , status = 1 )[:3]
    context = {"posts":posts , "Artists":Artists}
    return render(request, "webArt/index.html" , context )

def view_contact(request):
    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid(): 
            form.save()

    form = Contactform()
    return render(request , "webArt/contact.html" , {"form":form } ) 
