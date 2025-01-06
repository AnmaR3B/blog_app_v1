from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','author','publish','status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    #for slug ex: title = first post 
    #so slug will be slug= first-post
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    #filtering using date
    date_hierarchy = 'publish'
    ordering = ['status', 'publish','title']