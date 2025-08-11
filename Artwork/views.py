from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from Artwork.models import Artwork ,Comments
from Artwork.forms import Commentform
from django.utils import timezone
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#@login_required(login_url="/Accounts/login")
def view_Artwork(request , cate=None , tag=None):
    time_now=timezone.localtime(timezone.now())
    Arts = Artwork.objects.filter(poblished_date__lte=time_now , status = 1 )
    if cate:
        Arts = Arts.filter(category__name=cate)
    if tag:
        Arts = Arts.filter(tags__name=tag)
    
    Arts = Paginator(Arts , 4)
    try:
        page_number=request.GET.get('page')
        Arts = Arts.get_page(page_number)
    except EmptyPage:
        Arts = Arts.get_page(1)
    except PageNotAnInteger:
        Arts = Arts.get_page(1)

    context = {"Arts":Arts}
    return render(request, "Artwork/Artworks-page.html" , context)

def view_single_Artwork(request , pid):
    if request.method == "POST":
        form = Commentform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS , " SUBMITED! Thank you ")
        else:
            messages.add_message(request , messages.ERROR , " The information is incomplete . Please try again")
    form = Commentform()
    #post = Post.objects.get(id = pid)
    time_now=timezone.localtime(timezone.now())
    Arts = Artwork.objects.filter(poblished_date__lte=time_now , status = 1 ) 
    Art = get_object_or_404(Arts , pk=pid )
    # get comments
    comments = Comments.objects.filter(post=Art.id , approved=True)
    if not Art.login_require:
        # create a def for count post views
        def addview(Art):
            Art.content_view += 1
            return Art.save() 
        addview(Art)
        context = {"Art":Art , "Arts":Arts , "comments":comments , "form":form } 
        return render(request, "Artwork/Artwork-page.html" , context)
    else:
        return render(request,"Accounts/login.html")
