from django.urls import path
from Artgallery.views import *

app_name = "Artgallery"
urlpatterns = [
    path("", view_Artgallery, name="gallery"),
    path("<int:pid>", view_single_gallery, name="single-gallery"),
]
