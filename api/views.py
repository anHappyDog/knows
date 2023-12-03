from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from .models import User, Article, Category, Image, Video, Comment, Like, Follow
from django.views.decorators.http import require_http_methods

default_cover = "/"
default_avatar = "/"

@csrf_exempt
@require_http_methods('GET')
def test (request):
    return JsonResponse({"message":"test"})


@csrf_exempt
@require_http_methods('POST')
def signIn(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
    except Exception as e:
        return JsonResponse({"message":"未知错误","status": -1})
    try:
        user = User.objects.get(username=username)
    except:
        return JsonResponse({"message":"用户名不存在","status": -1})
    try:
        if 'username' in request.session:
            susername = request.session['username']
            if susername != username:
                return JsonResponse({"message":"未知错误","status": -1})
            return JsonResponse({"message":"成功登录","status": 0})
        if check_password(password, user.password):
            return JsonResponse({"message":"成功登录","status": 0})
        else:
            return JsonResponse({"message":"密码错误","status": -1})
    except Exception as e:
        return JsonResponse({"message":"未知错误","status": -1})    




@csrf_exempt
@require_http_methods('POST')
def signUp(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
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
def userInfo(request,id):
    try:
        user = User.objects.get(id=id)
        return JsonResponse({"message":"成功获取用户信息","status": 0,"data":{"username":user.username,"email":user.email,"avatar":user.avatar.url 
                                                                      if user.avatar is not None else default_avatar,"cover":user.cover.url if user.cover is not None else default_cover,"introduction":user.introduction}})
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
def getArticles(request):
    try:
        articles = Article.objects.all()
        data = []
        for article in articles:
            data.append({"id":article.id,"title":article.title,"date":article.date,"author":article.author.username,"category":article.category.name})
        return JsonResponse({"message":"成功获取文章列表","status": 0,"data":data})
    except:
        return JsonResponse({"message":"未知错误","status": -1})


@csrf_exempt
@require_http_methods('GET')
def getArticleDetails(request):
    try:
        id = request.GET.get('id')
        article = Article.objects.get(id=id)
        data = {"id":article.id,"title":article.title,"date":article.date,"author":article.author.username,"category":article.category.name,"content":article.content,"cover":article.cover.url if article.cover is not None else default_cover}
        return JsonResponse({"message":"成功获取文章详情","status": 0,"data":data})
    except:
        return JsonResponse({"message":"未知错误","status": -1})
    
@csrf_exempt
@require_http_methods('POST')
def writeArticle(request):
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        category = request.POST.get('category')
        cover = request.FILES.get('cover')
        user = User.objects.get(username=author)
        category = Category.objects.get(name=category)
        article = Article.objects.create(title=title, content=content, author=user, category=category, cover=cover)
        return JsonResponse({"message":"成功写入文章","status": 0})
    except:
        return JsonResponse({"message":"未知错误","status": -1})


@csrf_exempt
@require_http_methods('POST')
def updateArticle(request):
    try:
        id = request.POST.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        cover = request.FILES.get('cover')
        article = Article.objects.get(id=id)
        article.title = title
        article.content = content
        article.category = Category.objects.get(name=category)
        if cover is not None:
            article.cover = cover
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
    pass 


@csrf_exempt
@require_http_methods('POST')
def deleteComment(request):
    pass 

        
@csrf_exempt
@require_http_methods('POST')
def addLike(request):
    pass



@csrf_exempt
@require_http_methods('POST')
def deleteLike(request):
    pass


@csrf_exempt
@require_http_methods('POST')
def uploadAvatar(request):
    pass

@csrf_exempt
@require_http_methods('POST')
def uploadUserCover(request):
    pass 

@csrf_exempt
@require_http_methods('POST')
def uploadArticleCover(request):
    pass


@csrf_exempt
@require_http_methods('POST')
def signOut(request):
    pass



    