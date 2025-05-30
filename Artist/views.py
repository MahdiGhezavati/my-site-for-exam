from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render , get_object_or_404 , redirect
from Artist.models import Post 
from django.utils import timezone
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#@login_required(login_url="/accounts/login")
def view_Artist(request , cate=None , author_user=None , tag=None):
    time_now=timezone.localtime(timezone.now())
    posts = Post.objects.filter(poblished_date__lte=time_now , status = 1 )
    if author_user:
        posts = posts.filter(author__username = author_user)
    '''
    if tag:
        posts = posts.filter(tags__name=tag)
    '''
    posts = Paginator(posts , 2)
    try:
        page_number=request.GET.get('page')
        posts = posts.get_page(page_number)
    except EmptyPage:
        posts = posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)

    context = {"posts":posts}
    return render(request, "Artist/Artist-page.html" , context)

def single_page(request , pid):
    #post = Post.objects.get(id = pid)
    time_now=timezone.localtime(timezone.now())
    posts = Post.objects.filter(poblished_date__lte=time_now , status = 1 ) 
    post = get_object_or_404(posts , pk=pid )
    if not post.login_require:
        # create a def for count post views
        def addview(post):
            post.content_view += 1
            return post.save() 
        addview(post)
        context = {"post":post} 
        return render(request, "Artist/Artists-page.html" , context)
    else:
        return render(request,"accounts/login.html")