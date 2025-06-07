from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    artist = models.CharField(max_length=255)
    image  = models.ImageField(upload_to="media/Art" , default="media/Art/default.jpg")
    tags = TaggableManager()
    category = models.ManyToManyField(category)
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
        return reverse('Artwork:single',kwargs={'pid': self.id})

class Comments(models.Model):
    post = models.ForeignKey(Artwork,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
