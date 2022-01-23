from django.contrib import admin
from .models import post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","update","timestamp"]
    list_filter = ['update','timestamp']
    search_fields = ["title","content"]
    class Meta:
        model = post
admin.site.register(post, PostModelAdmin)
