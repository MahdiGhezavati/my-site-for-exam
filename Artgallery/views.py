from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from Artgallery.models import ArtGallery
from django.utils import timezone

def view_Artgallery(request):
    time_now=timezone.localtime(timezone.now())
    Arts = ArtGallery.objects.filter(poblished_date__lte=time_now , status = 1 )

    context = {"Arts":Arts}
    return render(request, "Artgallery/Artgallery.html",context)

def view_single_gallery(request , pid):
    time_now=timezone.localtime(timezone.now())
    Arts = ArtGallery.objects.filter(poblished_date__lte=time_now , status = 1 ) 
    Art = get_object_or_404(Arts , pk=pid )
    def addview(Art):
        Art.content_view += 1
        return Art.save() 
    addview(Art)
    context = {"Art":Art} 
    return render(request, "Artgallery/single-gallery.html" , context)
