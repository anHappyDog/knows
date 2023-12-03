from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.FileField(upload_to='videos/')
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table="video"




class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table="image"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=128)
    avatar = models.ForeignKey(Image, on_delete=models.CASCADE,related_name="user_avatar",null=True)
    cover = models.ForeignKey(Image, on_delete=models.CASCADE,related_name="user_cover",null=True)
    introduction = models.TextField(default="这个人很懒,连个人介绍都没有")
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table="user"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table="category"


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.ForeignKey(Image, on_delete=models.CASCADE,related_name="article_cover",null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title
    class Meta:
        db_table="article"

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.content
    class Meta:
        db_table="comment"

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.author.name
    class Meta:
        db_table="like"

class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")
    def __str__(self) -> str:
        return self.follower.name
    class Meta:
        db_table="follow"