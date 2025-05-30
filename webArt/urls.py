from django.urls import path
from webArt.views import *

app_name = "webArt"
urlpatterns = [
    path("" , view_home , name="index"),
    path("contact" , view_contact ,name= "contact"),

]
