from django.contrib import admin
from Artist.models import Post 
from django_summernote.admin import SummernoteModelAdmin

class Postadmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-"
    list_display = ["title","author","status","login_require","content_view" , "poblished_date","created_date"]
    list_filter = ["status","author","created_date"]
    #ordering = ["created_date"]
    search_fields = ["title" ,"content"]
    summernote_fields = ("content")


admin.site.register(Post , Postadmin)