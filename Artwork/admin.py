from django.contrib import admin
from Artwork.models import Artwork , category , Comments
from django_summernote.admin import SummernoteModelAdmin

class ArtworkAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-"
    list_display = ["id","title","artist","status","login_require","content_view" , "poblished_date","created_date"]
    list_filter = ["status","artist","created_date"]
    #ordering = ["created_date"]
    search_fields = ["title" ,"content"]
    summernote_fields = ("content")

class CommentAdmin(admin.ModelAdmin ):
    date_hierarchy = "created_date"
    list_display = ["name","post","approved","email"]
    search_fields = ["name" , "subect"]
    list_filter = ["approved"]
    empty_value_display = "-"


admin.site.register(Comments,CommentAdmin)
admin.site.register(category)
admin.site.register(Artwork , ArtworkAdmin)