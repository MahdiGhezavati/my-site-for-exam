from django.urls import path
from Artist.views import *

app_name = "Artist"
urlpatterns = [
    path("", view_Artist, name="blog-Artist"),
    path("<int:pid>", single_page, name="single"),
    path("tag/<str:tag>", view_Artist, name="tag"),
]
