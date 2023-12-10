from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timezone
import uuid 
import os
# Create your models here.


def generateName():
    return str(uuid.uuid4())[:16]
def upload_to_videos(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = "{}.{}".format(generateName(), ext)
    return os.path.join('videos', new_filename)

def upload_to_images(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = "{}.{}".format(generateName(), ext)
    return os.path.join('images', new_filename)


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,db_index=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title    
    class Meta:
        db_table="feedback"


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.FileField(upload_to=upload_to_videos)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=32,default=generateName)
    preview = models.ForeignKey('Image', on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table="video"



class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to=upload_to_images)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=32,default=generateName)
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
    admin = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table="user"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True,db_index=True)
    description = models.TextField(default="创建这个板块的人很懒,连板块介绍都没有!")
    image = models.ForeignKey(Image, on_delete=models.CASCADE,related_name="category_image",null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table="category"


class FeedbackPost(models.Model):
    id = models.AutoField(primary_key=True)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE,db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="feedback_post"


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,db_index=True)
    content = models.TextField()
    cover = models.ForeignKey(Image, on_delete=models.CASCADE,related_name="article_cover",null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title
    class Meta:
        db_table="article"

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.content
    class Meta:
        db_table="comment"

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    likedUser = models.ForeignKey(User, on_delete=models.CASCADE)
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

class UserImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.name
    class Meta:
        db_table="user_image"

class UserVideo(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.name
    class Meta:
        db_table="user_video"
