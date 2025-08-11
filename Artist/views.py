from django.shortcuts import render , get_object_or_404 , redirect
from Artist.models import Artist 
from Artwork.models import Artwork
from django.utils import timezone
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#@login_required(login_url="/accounts/login")
def view_Artist(request , author_user=None , tag=None):
    time_now=timezone.localtime(timezone.now())
    Arts = Artist.objects.filter(poblished_date__lte=time_now , status = 1 )
    Artworks = Artwork.objects.filter(poblished_date__lte=time_now , status= 1 )
    if author_user:
        Arts = Arts.filter(author__username = author_user)
    if tag:
        Arts = Arts.filter(tags__name=tag)

    Arts = Paginator(Arts , 2)
    try:
        page_number=request.GET.get('page')
        Arts = Arts.get_page(page_number)
    except EmptyPage:
        Arts = Arts.get_page(1)
    except PageNotAnInteger:
        Arts = Arts.get_page(1)

    context = {"Arts":Arts , "Artworks":Artworks }
    return render(request, "Artist/Artist-page.html" , context)

def single_page(request , pid):
    #post = Post.objects.get(id = pid)
    time_now=timezone.localtime(timezone.now())
    posts = Artist.objects.filter(poblished_date__lte=time_now , status = 1 ) 
    artist = get_object_or_404(posts , pk=pid )
    Art_of_artist = Artwork.objects.filter(poblished_date__lte=time_now , status= 1 , artist=artist.title )
    if not artist.login_require:
        # create a def for count post views
        def addview(artist):
            artist.content_view += 1
            return artist.save() 
        addview(artist)
        context = {"artist":artist , "works":Art_of_artist} 
        return render(request, "Artist/Artists-page.html" , context)
    else:
        return render(request,"accounts/login.html")