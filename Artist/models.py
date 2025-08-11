from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Artist(models.Model):
    author = models.ForeignKey(User , on_delete=models.SET_NULL,null=True)
    image  = models.ImageField(upload_to="Artist" , default="media/Artist/default.jpg")
    title = models.CharField(max_length=255)
    content = models.TextField()
    content_view = models.IntegerField(default = 1)
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    poblished_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # filter for content of post with word 
    def snippet(self):
        listk=self.content.split(" ")
        listk=listk[:5]
        return " ".join(map(str , listk)) + ". . ."


    class Meta:
        ordering = ["created_date"]
 
    def __str__(self):
        return f" {self.id} - {self.title} "
    
    def get_absolute_url(self):
        return reverse('Artist:single',kwargs={'pid': self.id})
    