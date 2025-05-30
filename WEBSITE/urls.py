from django.contrib import admin
from django.urls import path , include
from django.conf import settings

from django.conf.urls.static import static # for static and media 
from django.views.generic.base import TemplateView # for MAINTENANCE_MODE 
from django.urls import re_path # for MAINTENANCE_MODE 


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("webArt.urls")),
    path("Accounts/", include("Accounts.urls")),  
    path("Artwork/", include("Artwork.urls")),
    path("Artist/", include("Artist.urls")),
    #path("sitemap.xml",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap",),
    #path("robots.txt" , include("robots.urls")),
    path("summernote/" , include("django_summernote.urls")),
    #path("captcha" , include("captcha.urls")),
]
if settings.MAINTENANCE_MODE:
   urlpatterns.insert(0, re_path(r'^', TemplateView.as_view(template_name='503.html'), name='maintenance'))

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)