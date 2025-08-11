from django.contrib import admin
from Artgallery.models import ArtGallery
from django_summernote.admin import SummernoteModelAdmin ,models

class ArtGalleryAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-"
    list_display = ["title","artist","status","content_view" , "poblished_date","created_date"]
    list_filter = ["status","artist","created_date"]


admin.site.register(ArtGallery , ArtGalleryAdmin)