from django.urls import path
from Artwork.views import *

app_name = "Artwork"
urlpatterns = [
    path("", view_Artwork, name="Artwork"),
    path("<int:pid>", view_single_Artwork, name="single-Artwork"),
    path("tag/<str:tag>", view_Artwork, name="tag"),
    path("category/<str:cate>", view_Artwork, name="category"),
]
