from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from Artwork.models import Artwork ,Comments
from Artwork.forms import Commentform
from django.utils import timezone
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#@login_required(login_url="/Accounts/login")
def view_Artwork(request , cate=None , author_user=None , tag=None):
    time_now=timezone.localtime(timezone.now())
    posts = Artwork.objects.filter(poblished_date__lte=time_now , status = 1 )
    if cate:
        posts = posts.filter(category__name=cate)
    if tag:
        posts = posts.filter(tags__name=tag)
    
    posts = Paginator(posts , 4)
    try:
        page_number=request.GET.get('page')
        posts = posts.get_page(page_number)
    except EmptyPage:
        posts = posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)

    context = {"posts":posts}
    return render(request, "Artwork/Artworks-page.html" , context)

def view_single_Artwork(request , pid):
    if request.method == "POST":
        form = Commentform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS , " SUBMITED! " , extra_tags="succ")
        else:
            messages.add_message(request , messages.ERROR , "plaese try again ! " , extra_tags="error")
    form = Commentform()
    #post = Post.objects.get(id = pid)
    time_now=timezone.localtime(timezone.now())
    posts = Artwork.objects.filter(poblished_date__lte=time_now , status = 1 ) 
    post = get_object_or_404(posts , pk=pid )
    # get comments
    comments = Comments.objects.filter(post=post.id , approved=True)
    if not post.login_require:
        # create a def for count post views
        def addview(post):
            post.content_view += 1
            return post.save() 
        addview(post)
        context = {"post":post , "posts":posts , "comments":comments , "form":form } 
        return render(request, "Artwork/Artwork-page.html" , context)
    else:
        return render(request,"Accounts/login.html")
