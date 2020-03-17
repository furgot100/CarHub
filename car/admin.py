from django.contrib import admin

from car.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'modified')


admin.site.register(Post, PostAdmin)