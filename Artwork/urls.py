from django.urls import path
from Artist.views import *

app_name = "Artwork"
urlpatterns = [
    path("" , view_Artist , name="Artwork"),
    path("<int:pid>" , single_page , name= 'single'),

]