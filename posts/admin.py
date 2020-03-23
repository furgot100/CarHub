from django.contrib import admin
from posts.models import Post, Products

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title','slug', 'author', 'created', 'modified')
admin.site.register(Post)
admin.site.register(Products)
