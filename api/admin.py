from django.contrib import admin
from .models import User, Article, Category, Image, Video, Comment, Like, Follow
# Register your models here.

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)
