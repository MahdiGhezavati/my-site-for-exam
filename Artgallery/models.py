from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ArtGallery(models.Model):
    artist = models.CharField(max_length=255)
    image  = models.ImageField(upload_to="gallery")
    title = models.CharField(max_length=255)
    content_view = models.IntegerField(default = 1)
    status = models.BooleanField(default=False)
    poblished_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["created_date"]
 
    def __str__(self):
        return f" {self.id} - {self.title} "
    '''
    def get_absolute_url(self):
        return reverse('Artwork:single-Artwork',kwargs={'pid': self.id})'''