from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from .models import User, Article, Category, Image, Video, Comment, Like, Follow,Feedback,FeedbackPost
from .models import UserImage,UserVideo
from django.views.decorators.http import require_http_methods
from django.utils.timesince import timesince
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.images import ImageFile
import subprocess
import json
import uuid
default_cover = "/static/images/default_cover.jpg"
default_avatar = "/static/images/default_avatar.jpg"
default_category_image = "/static/images/default_avatar.jpg"

@csrf_exempt
@require_http_methods('GET')
def test (request):
    return JsonResponse({"message":"test"})



@require_http_methods('GET')
def getArticleContent(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        id = request.GET.get('id')
        article = Article.objects.get(id=id)
        return JsonResponse({"message":"成功获取文章内容","status": 0,"data":{
            "title":article.title,"content":article.content,"category":article.category.name}})
    except:
        return JsonResponse({"message":"未知错误","status": -1})


@require_http_methods('POST')
def updateArticle(reqeust):
    try:
        if 'username' not in reqeust.session:
            return JsonResponse({"message":"未登录","status": -1})
        data = json.loads(reqeust.body)
        id = data.get('id')
        title = data.get('title')
        content = data.get('content')
        category = data.get('category')
        cover = None
        if 'cover' in reqeust.FILES:
            cover = reqeust.FILES.get('cover')
        article = Article.objects.get(id=id)
        article.title = title
        article.content = content
        article.category = Category.objects.get(name=category)
        if cover is not None:
            if article.cover is not None:
                article.cover.delete()
            article.cover = Image.objects.create(image=cover)
        article.save()
        return JsonResponse({"message":"成功更新文章","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})



@csrf_exempt
@require_http_methods('GET')
def getUserVideos(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        user = User.objects.get(username=request.session['username'])
        videos = UserVideo.objects.filter(user=user)
        data = []
        for video in videos:
            data.append({"id":video.id,"video":video.video.video.url,"preview":video.video.preview.image.url if video.video.preview is not None else default_cover})
        return JsonResponse({"message":"成功获取用户视频","status": 0,"data":data})
    except:
        
        return JsonResponse({"message":"未知错误","status": -1})

@csrf_exempt
@require_http_methods('GET')
def getUserImages(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        user = User.objects.get(username=request.session['username'])
        images = UserImage.objects.filter(user=user)
        data = []
        for image in images:
            data.append({"id":image.id,"image":image.image.image.url})
        return JsonResponse({"message":"成功获取用户图片","status": 0,"data":data})
    except Exception as e:
        return JsonResponse({"message":str(e),"status": -1})

@csrf_exempt
@require_http_methods('POST')
def signIn(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
    except Exception as e:
        return JsonResponse({"message":"未知错误","status": -1})
    try:
        user = User.objects.get(username=username)
    except:
        return JsonResponse({"message":"用户名不存在","status": -1})
    try:
        if check_password(password, user.password):
            request.session['username'] = username
            print(request.session.keys())
            return JsonResponse({"message":"成功登录","status": 0,'token':user.id})
        else:
            return JsonResponse({"message":"密码错误","status": -1})
    except Exception as e:
        return JsonResponse({"message":"未知错误","status": -1})    




@csrf_exempt
@require_http_methods('POST')
def signUp(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        print(username,password,email)
    except:
        return JsonResponse({"message":"未知错误","status": -1})
    try:
        user = User.objects.filter(username=username)
        if len(user) > 0:
            return JsonResponse({"message":"用户名已存在","status": -1})
        user = User.objects.filter(email=email)
        if len(user) > 0:
            return JsonResponse({"message":"邮箱已存在","status": -1})
        password = make_password(password)
        user = User.objects.create(username=username, password=password, email=email)
        return JsonResponse({"message":"成功注册","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})
    
    
@csrf_exempt
@require_http_methods('GET')
def getFeedbacks(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        feedbacks = Feedback.objects.all()
        data = []
        for feedback in feedbacks:
            data.append({"id":feedback.id,"title":feedback.title,"user_avatar":feedback.user.avatar.image.url if feedback.user.avatar is not None else default_avatar,
                         "created_time":timesince(feedback.date),"user":feedback.user.username,"content":feedback.content,"user_id":feedback.user.id,})
        return JsonResponse({"message":"成功获取反馈列表","status": 0,"data":data,"admin":User.objects.get(username=request.session['username']).admin})
    except:
        return JsonResponse({"message":"未知错误","status": -1})

@csrf_exempt
@require_http_methods('POST')
def newFeedback(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')
        user = User.objects.get(username=request.session['username'])
        print("tttt")
        feedback = Feedback.objects.create(title=title,content=content,user=user)
        return JsonResponse({"message":"成功提交反馈","status": 0})
    except Exception as e:
        return JsonResponse({"message":str(e),"status": -1})
 
@csrf_exempt
@require_http_methods('GET')
def getFeedbackPosts(request,feedback_id):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})

        feedback = Feedback.objects.get(id=feedback_id)

        posts = FeedbackPost.objects.filter(feedback=feedback)
        data = []
        
        for post in posts:
            data.append({"id":post.id,"content":post.content,"created_time":timesince(post.date),"user":post.user.username,
                         'user_id':post.user.id,"user_avatar":post.user.avatar.image.url if post.user.avatar is not None else default_avatar})
        return JsonResponse({"message":"成功获取反馈回复列表","status": 0,"data":data})
    except Exception as e:
        return JsonResponse({"message":str(e),"status": -1})
 
@csrf_exempt
@require_http_methods('POST')
def newFeedbackPost(request,feedback_id):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        feedback = Feedback.objects.get(id=feedback_id)
        user = User.objects.get(username=request.session['username'])
        if not user.admin and not feedback.user.username == request.session['username']:
            return JsonResponse({"message":"权限不足","status": -1})
        data = json.loads(request.body)
        content = data.get('content')
        post = FeedbackPost.objects.create(feedback=feedback,user=user,content=content)
        return JsonResponse({"message":"成功提交回复","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})
 
@csrf_exempt
@require_http_methods('GET')
def getFeedback(request,feedback_id):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        user =User.objects.get(username=request.session['username'])
        feedback = Feedback.objects.get(id=feedback_id)
        return JsonResponse({"message":"成功获取反馈","status": 0,"admin":user.admin,"data":{"id":feedback.id,"title":feedback.title,"content":feedback.content,
                        "can_answer": user.admin or feedback.user.username == request.session['username'],
                        "created_time":timesince(feedback.date),"user":feedback.user.username,"user_id":feedback.user.id,
                        "user_avatar": feedback.user.avatar.image.url if feedback.user.avatar is not None else default_avatar}})
    except:
        return JsonResponse({"message":'未知错误',"status": -1})
 

@csrf_exempt
@require_http_methods('GET')
def getUserInfo(request,id):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        curUser =  User.objects.get(username=request.session['username'])
        user = User.objects.get(id=id)
        followed = len(Follow.objects.filter(follower=curUser,followed=user)) == 1
        return JsonResponse({"message":"成功获取用户信息","status": 0,"data":{"username":user.username,"email":user.email,"avatar":user.avatar.image.url
                                                                      if user.avatar is not None else default_avatar,
                                                                      "cover":user.cover.image.url if user.cover is not None else default_cover,
                                                                      "introduction":user.introduction,"is_followed":followed,"isSelf":user.username == request.session['username']}})
    except:
        return JsonResponse({"message":"未知错误","status": -1})


@csrf_exempt
@require_http_methods('POST')
def followSomeone(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        data = json.loads(request.body)
        user_id = data.get('user_id')
        user = User.objects.get(id=user_id)
        curUser = User.objects.get(username=request.session['username'])
        if (user.username == curUser.username):
            return JsonResponse({"message":"不能关注自己","status": -1})
        if len(Follow.objects.filter(follower=curUser,followed=user)) > 0:
            return JsonResponse({"message":"已经关注过了","status": -1})
        follow = Follow.objects.create(follower=curUser,followed=user)
        return JsonResponse({"message":"成功关注","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})

@csrf_exempt
@require_http_methods('GET')
def getFollows(request,user_id):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        user = User.objects.get(id=user_id)
        follows = Follow.objects.filter(followed=user)
        data = []
        for follow in follows:
            
            data.append({"is_followed":len(Follow.objects.filter(followed=follow.follower,follower=user)) == 1,"id":follow.follower.id,"username":follow.follower.username,"email":follow.follower.email,"avatar":follow.follower.avatar.image.url
                                                                      if follow.follower.avatar is not None else default_avatar})
        return JsonResponse({"message":"成功获取关注列表","status": 0,"data":data})
    except Exception as e:
        return JsonResponse({"message":str(e),"status": -1})

@csrf_exempt
@require_http_methods('GET')
def getFollowees(request,user_id):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        user = User.objects.get(id=user_id)
        follows = Follow.objects.filter(follower=user)
        data = []
        for follow in follows:
            data.append({"id":follow.followed.id,"username":follow.followed.username,"email":follow.followed.email,"avatar":follow.followed.avatar.image.url
                                                                      if follow.followed.avatar is not None else default_avatar})
        print(data)
        return JsonResponse({"message":"成功获取关注列表","status": 0,"data":data})
    except Exception as e:
        return JsonResponse({"message":str(e),"status": -1})

@csrf_exempt
@require_http_methods('POST')
def unfollowSomeone(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        data = json.loads(request.body)
        user_id = data.get('user_id')
        user = User.objects.get(id=user_id)
        curUser = User.objects.get(username=request.session['username'])
        if (user.username == curUser.username):
            return JsonResponse({"message":"不能取消关注自己","status": -1})
        follow = Follow.objects.filter(follower=curUser,followed=user)
        if len(follow) == 0:
            return JsonResponse({"message":"还没有关注","status": -1})
        follow.delete()
        return JsonResponse({"message":"成功取消关注","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})    

    
@csrf_exempt
@require_http_methods('POST')
def updateUserInfo(request,id):
    try:
        user = User.objects.get(id=id)
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.introduction = request.POST.get('introduction')
        user.save()
        return JsonResponse({"message":"成功更新用户信息","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})


@csrf_exempt
@require_http_methods('GET')
def getArticlesWithKeyword(request,keyword):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        articles = Article.objects.filter(title__contains=keyword)
        data = []
        for article in articles:
            data.append({"id":article.id,"title":article.title,"date":timesince(article.date), 
                         "author_avatar":article.author.avatar.image.url if article.author.avatar is not None else default_avatar,
                            "author_id":article.author.id,
                            "author":article.author.username,"category":article.category.name,"category_id":article.category.id})
        return JsonResponse({"message":"成功搜索文章","status": 0,"data":data})
    except:
        return JsonResponse({"message":"未知错误","status": -1})

@csrf_exempt
@require_http_methods('GET')
def getArticles(request,category_id=None,user_id=None):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        data = []
        categoryInfo = {}
        if category_id is not None:
            articles = Article.objects.filter(category=Category.objects.get(id=category_id))
            category = Category.objects.get(id=category_id)
            categoryInfo = {"id":category.id,"name":category.name,"description":category.description,"created_time":category.created_time.strftime('%y-%m-%d'),
                            "image":category.image.image.url if category.image is not None else default_category_image}
        elif user_id is not None:
            articles = Article.objects.filter(author=User.objects.get(id=user_id))
        else:
            articles = Article.objects.all()
        for article in articles:
                data.append({"id":article.id,"title":article.title,"date":timesince(article.date),
                             "author_avatar":article.author.avatar.image.url if article.author.avatar is not None else default_avatar,
                             "author_id":article.author.id,
                             "author":article.author.username,"category":article.category.name,"category_id":article.category.id})
        response = {"message":"成功获取文章列表","status": 0,"data":data}
        if category_id is not None:
            response['categoryInfo'] = categoryInfo
        return JsonResponse(response)
    except:
        return JsonResponse({"message":"未知错误","status": -1})


@csrf_exempt
@require_http_methods('GET')
def getArticleDetails(request,article_id):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        user = User.objects.get(username=request.session['username'])
        article = Article.objects.get(id=article_id)
        likes = Like.objects.filter(article=article,likedUser=user)
        isAuthor = article.author.username == request.session['username']
        liked = len(likes) == 1
        likes = len(Like.objects.filter(article=article))
        data = {"id":article.id,"title":article.title,"date":article.date,"author":article.author.username,
                "author_avatar":article.author.avatar.image.url if article.author.avatar is not None else default_avatar,
                "category":article.category.name,"content":article.content,"created_time":timesince(article.created_time),
                "cover":article.cover.image.url if article.cover is not None else default_cover,"liked": liked,
                "isAuthor":isAuthor,"author_id":article.author.id,"category_id":article.category.id,"likes":likes
                }
        return JsonResponse({"message":"成功获取文章详情","status": 0,"data":data})
    except:
        return JsonResponse({"message":"未知错误","status": -1})

@csrf_exempt
@require_http_methods('GET')
def getLikes(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        article_id = request.GET.get('article_id')
        article = Article.objects.get(id=article_id)
        likes = len(Like.objects.filter(article=article))
        
        return JsonResponse({"message":"成功获取点赞列表","status": 0,"likes":likes})
    except:
        return JsonResponse({"message":"未知错误","status": -1})

@csrf_exempt
@require_http_methods('POST')
def writeArticle(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        category_id = request.POST.get('category_id')
        
        cover = None
        if 'cover' in request.FILES:
            cover = request.FILES.get('cover')
            cover = Image.objects.create(image=cover)
        user = User.objects.get(username=request.session['username'])
        category = Category.objects.get(id=category_id)
        article = Article.objects.create(title=title, content=content, author=user, category=category, cover=cover)
        return JsonResponse({"message":"成功写入文章","status": 0,'data':{"id":article.id}})
    except:
        return JsonResponse({"message":"未知错误","status": -1})


@csrf_exempt
@require_http_methods('POST')
def updateArticle(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        username = request.session['username']
        user = User.objects.get(username=username)
        id = request.POST.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        cover = None
        if 'cover' in request.FILES:
            cover = request.FILES.get('cover')
        article = Article.objects.get(id=id)
        if user != article.author:
            return JsonResponse({"message":"权限不足","status": -1})
        article.title = title
        article.content = content
        article.category = Category.objects.get(name=category)
        if cover is not None:
            if article.cover is not None:
                article.cover.delete()
            article.cover = Image.objects.create(image=cover)
        article.save()
        return JsonResponse({"message":"成功更新文章","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})
    
@csrf_exempt
@require_http_methods('POST')
def deleteArticle(request):
    try:
        id = request.POST.get('id')
        article = Article.objects.get(id=id)
        article.delete()
        return JsonResponse({"message":"成功删除文章","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})

@csrf_exempt
@require_http_methods('POST')
def ChangeUserInfo(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        username = request.session['username']
        user = User.objects.get(username=username)
        data = json.loads(request.body)

        user.email = data.get('email')
        user.introduction = data.get('introduction')
        user.save()
        return JsonResponse({"message":"成功更新用户信息","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})


@csrf_exempt
@require_http_methods('GET')
def searchArticles(request):
    try:
        keyword = request.GET.get('keyword')
        articles = Article.objects.filter(title__contains=keyword)
        data = []
        for article in articles:
            data.append({"id":article.id,"title":article.title,"date":article.date,"author":article.author.username,"category":article.category.name})
        return JsonResponse({"message":"成功搜索文章","status": 0,"data":data})
    except:
        return JsonResponse({"message":"未知错误","status": -1}).charset
    
    
@csrf_exempt
@require_http_methods('POST')
def addComment(request):
    try:
        data = json.loads(request.body)
        article_id = data.get('article_id')
        content = data.get('content')
        article = Article.objects.get(id=article_id)
        user = User.objects.get(username=request.session['username'])
        comment = Comment.objects.create(content=content,article=article,commentUser=user)
        return JsonResponse({"message":"成功添加评论","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})


@csrf_exempt
@require_http_methods('POST')
def deleteComment(request):
    try:

        data = json.loads(request.body)
  
        comment_id = data.get('comment_id')
        print(comment_id)
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return JsonResponse({"message":"成功删除评论","status": 0}) 
    except Exception as e:
        return JsonResponse({"message":str(e),"status": -1})

@csrf_exempt
@require_http_methods('GET')
def getComments(reqeust):
    try:
        if 'username' not in reqeust.session:
            return JsonResponse({"message":"未登录","status": -1})
        article_id = reqeust.GET.get('article_id')
        article = Article.objects.get(id=article_id)
        comments = Comment.objects.filter(article=article)
        data = []
        for comment in comments:
            data.append({"id":comment.id,"content":comment.content,"created_time":timesince(comment.date),"commentUser":comment.commentUser.username,
        'canDelete':comment.commentUser.username == reqeust.session['username'] or comment.article.author.username == reqeust.session['username'],
        'user_avatar': comment.commentUser.avatar.image.url if comment.commentUser.avatar is not None else default_avatar,
        'user_id':comment.commentUser.id
        })
        return JsonResponse({"message":"成功获取评论列表","status": 0,"data":data})
    except:
        return JsonResponse({"message":"未知错误","status": -1})

        
@csrf_exempt
@require_http_methods('POST')
def addLike(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        data = json.loads(request.body)
        article_id = data.get('article_id')
        article = Article.objects.get(id=article_id)
        user = User.objects.get(username=request.session['username'])
        like = Like.objects.filter(article=article,likedUser=user)
        if len(like) > 0:
            return JsonResponse({"message":"已经点过赞了","status": -1})
        like = Like.objects.create(article=article,likedUser=user)
        return JsonResponse({"message":"成功点赞","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})



@csrf_exempt
@require_http_methods('POST')
def deleteLike(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        data = json.loads(request.body)
        article_id = data.get('article_id')
        article = Article.objects.get(id=article_id)
        user = User.objects.get(username=request.session['username'])
        like = Like.objects.filter(article=article,likedUser=user)
        if len(like) == 0:
            return JsonResponse({"message":"还没有点赞","status": -1})
        like.delete()
        return JsonResponse({"message":"成功取消点赞","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})


@csrf_exempt
@require_http_methods('POST')
def uploadAvatar(request):
    try:
        username = request.session.get('username')
        user = User.objects.get(username=username)
        avatar_file = request.FILES.get('avatar')
        if avatar_file is None:
            return JsonResponse({"message":"上传失败","status": -1})
        avatar = Image.objects.create(image=avatar_file)
        if user.avatar:
            user.avatar.delete()
        user.avatar = avatar
        
        user.save()
        return JsonResponse({"message":"成功上传头像","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})
    
@csrf_exempt
@require_http_methods('POST')
def uploadCover(request):
    try:
        username = request.session['username']
        user = User.objects.get(username=username)
        cover_file = request.FILES.get('cover')
        if cover_file is None:
            return JsonResponse({"message":"上传失败","status": -1})
        
        cover = Image.objects.create(image=cover_file)
        if user.cover:
            user.cover.delete()
        user.cover = cover
        print(user.cover.image.url)
        user.save()
        return JsonResponse({"message":"成功上传封面","status": 0})
    except Exception as e:
        return JsonResponse({"message":str(e),"status": -1})

@csrf_exempt
@require_http_methods('POST')
def uploadArticleCover(request):
    try:
        data = json.loads(request.body)
        article_id = data.get('article_id')
        article = Article.objects.get(id=article_id)
        cover_file = request.FILES.get('cover')
        if cover_file is None:
            return JsonResponse({"message":"上传失败","status": -1})
        cover = Image.objects.create(image=cover_file)
        if article.cover:
            article.cover.delete()
        article.cover = cover
        article.save()
        return JsonResponse({"message":"成功上传封面","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})

@csrf_exempt
@require_http_methods('POST')
def signOut(request):
    try:
        del request.session['username']
        return JsonResponse({"message":"成功登出","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})

@csrf_exempt
@require_http_methods('GET')
def getCategories(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        user = User.objects.get(username=request.session['username'])
        categories = Category.objects.all()
        data = []
        admin = user.admin
        for category in categories:
            data.append({"id":category.id,"name":category.name,"created_time":category.created_time.strftime('%y-%m-%d'),'description':category.description,"image":category.image.image.url if category.image is not None else default_category_image})
        print(request.session.keys())
        return JsonResponse({"message":"成功获取分类列表","status": 0,"data":data})
    except:
        return JsonResponse({"message":"未知错误","status": -1})
    

@csrf_exempt
@require_http_methods('GET')
def isAdmin(request):
    try:
        username = request.session['username']
        user = User.objects.get(username=username)
        return JsonResponse({"message":"成功获取用户信息","status": 0,"data":user.admin})
    except:
        return JsonResponse({"message":"未知错误","status": -1})
    

@csrf_exempt
@require_http_methods('POST')
def newCategory(request):
    try:
        username = request.session['username']
        user = User.objects.get(username=username)
        if not user.admin:
            return JsonResponse({"message":"权限不足","status": -1})
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = None
        if 'image' in request.FILES:
            image = request.FILES.get('image')
            image = Image.objects.create(image=image)
        if name is None:
            return JsonResponse({"message":"板块名不能为空","status": -1})
        if description is None:
            return JsonResponse({"message":"板块描述不能为空","status": -1})
        category = Category.objects.create(name=name,description=description,image=image)
        return JsonResponse({"message":"成功创建板块","status": 0})
    except Exception as e:
        return JsonResponse({"message":str(e),"status": -1})

@csrf_exempt
@require_http_methods('POST')
def deleteCategory(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        
        username = request.session['username']
        user = User.objects.get(username=username)
        if not user.admin:
            return JsonResponse({"message":"权限不足","status": -1})
        data = json.loads(request.body)
        id = data.get('category_id')
        category = Category.objects.get(id=id)
        articles = Article.objects.filter(category=category)
        if len(articles) != 0:
            return JsonResponse({"message":"该板块下还有文章，不能删除","status": -1})
        category.delete()
        return JsonResponse({"message":"成功删除板块","status": 0})
    except Exception as e:
        return JsonResponse({"message": str(e),"status": -1})

def extract_cover(file_path):
    cover_image_stream = BytesIO()

    # 构建 ffmpeg 命令来提取封面图像
    command = [
        'ffmpeg',
        '-i', file_path,  
        '-ss', '00:00:01',
        '-vframes', '1',
        '-f', 'image2',
        '-c:v', 'mjpeg',
        '-'
    ]
    # 运行 ffmpeg 命令
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    # print('FFmpeg stderr:', error.decode('utf-8'))
    # 将封面图像数据写入 BytesIO 流
    image_data = result.stdout
    image_file = BytesIO(image_data)
    
    # 将 BytesIO 流转换为 Django 可以处理的 UploadedFile
    file_name='cover.jpg'
    in_mem_file = ImageFile(image_file, name=file_name)

    return in_mem_file

#below are used for the articles
@csrf_exempt
@require_http_methods('POST')
def uploadUserVideo(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        username = request.session['username']
        user = User.objects.get(username=username)
        video_file = request.FILES.get('video')
        if video_file is None:
            return JsonResponse({"message":"上传失败","status": -1})
 
        video = Video.objects.create(video=video_file)
        #只能偷懒了
        cover_image_file = extract_cover(video.video.path)
        
        preview = Image.objects.create(image=cover_image_file)
        video.preview = preview
        video.save()
        UserVideo.objects.create(user=user,video=video)
        videos = UserVideo.objects.filter(user=user)
        data = []
        for video in videos:
            data.append({"id":video.id,"video":video.video.video.url,"preview":video.video.preview.image.url if video.video.preview is not None else default_cover})
        return JsonResponse({"message":"成功上传视频","data":data,"status": 0})
    except Exception as e:
        return JsonResponse({"message":str(e),"status": -1})

@csrf_exempt
@require_http_methods('POST')
def uploadUserImage(request):
    try:
        if 'username' not in request.session:
            return JsonResponse({"message":"未登录","status": -1})
        username = request.session['username']
        user = User.objects.get(username=username)
        image_file = request.FILES.get('image')
        print(request.FILES)
        if image_file is None:
            return JsonResponse({"message":"上传失败","status": -1})
        image = Image.objects.create(image=image_file)
        UserImage.objects.create(user=user,image=image)
        return JsonResponse({"message":"成功上传图片","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})

@csrf_exempt
@require_http_methods('POST')
def deleteUserVideo(request):
    try:
        username = request.session['username']
        user = User.objects.get(username=username)
        id = request.POST.get('id')
        video = Video.objects.get(id=id)
        video.delete()
        return JsonResponse({"message":"成功删除视频","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})
    
@csrf_exempt
@require_http_methods('POST')
def deleteUserImage(request):
    try:
        username = request.session['username']
        user = User.objects.get(username=username)
        id = request.POST.get('id')
        image = Image.objects.get(id=id)
        image.delete()
        return JsonResponse({"message":"成功删除图片","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})
