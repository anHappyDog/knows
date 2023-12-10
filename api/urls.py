from .views import test,signIn,signUp,getArticles,getArticleDetails,getUserInfo,getCategories
from .views import uploadArticleCover,uploadAvatar,uploadCover,signOut,isAdmin,newCategory
from .views import deleteCategory,writeArticle,addLike,deleteLike,getLikes,addComment
from .views import deleteComment,getComments,followSomeone,unfollowSomeone,getFollows,deleteArticle
from .views import getFollowees,getFeedbacks,newFeedback,getFeedback,getFeedbackPosts,updateArticle
from .views import uploadUserVideo,uploadUserImage,deleteUserImage,deleteUserVideo,ChangeUserInfo
from .views import newFeedbackPost,getUserImages,getUserVideos,getArticlesWithKeyword,getArticleContent
from django.urls import path


urlpatterns = [
    path('test', test,name="test"),
    path('signIn', signIn,name="signIn"),
    path('signUp', signUp,name="signUp"),
    path('articles', getArticles,name="getArticles"),
    path('articles/search/<str:keyword>', getArticlesWithKeyword,name="searchArticles"),
    path('article/<int:article_id>', getArticleDetails,name="getArticle"),
    path('user/<int:id>', getUserInfo,name="getUserInfo"),
    path('categories', getCategories,name="getCategories"),
    path('uploadArticleCover', uploadArticleCover,name="uploadArticleCover"),
    path('uploadAvatar', uploadAvatar,name="uploadAvatar"),
    path('uploadCover', uploadCover,name="uploadCover"),
    path('signOut', signOut,name="signOut"),
    path('admin', isAdmin,name="isAdmin"),
    path('newCategory', newCategory,name="newCategory"),
    path('delCategory', deleteCategory,name="deleteCategory"),
    path('category/<int:category_id>', getArticles,name="getArticlesByCategory"),
    path('newArticle',writeArticle,name="newArticle"),
    path('like',addLike,name="addLike"),
    path('unlike',deleteLike,name="deleteLike"),
    path('likes',getLikes,name="getLikes"),
    path('newComment',addComment,name="addComment"),
    path('delComment',deleteComment,name="deleteComment"),
    path('comments',getComments,name="getComments"),
    path('user/<int:user_id>/articles',getArticles,name="getArticlesByUser"),
    path('follow',followSomeone,name="followSomeone"),
    path('unfollow',unfollowSomeone,name="unfollowSomeone"),
    path('user/<int:user_id>/followers',getFollows,name="getFollows"),
    path('user/<int:user_id>/followees',getFollowees,name="getFollowees"),
    path('feedbacks',getFeedbacks,name="getFeedbacks"),
    path('feedback',newFeedback,name="newFeedback"),
    path('feedback/<int:feedback_id>',getFeedback,name="feedback"),
    path('uploadUserVideo',uploadUserVideo,name="uploadUserVideo"),
    path('uploadUserImage',uploadUserImage,name="uploadUserImage"),
    path('deleteUserVideo',deleteUserVideo,name="deleteUserVideo"),
    path('deleteUserImage',deleteUserImage,name="deleteUserImage"),
    path('feedback/<int:feedback_id>/posts',getFeedbackPosts,name="getFeedbackPosts"),
    path('feedback/<int:feedback_id>/test',newFeedbackPost,name="newFeedbackPost"),
    path('user/images',getUserImages,name="getUserImages"),
    path('user/videos',getUserVideos,name="getUserVideos"),
    path('changeUserInfo',ChangeUserInfo,name="ChangeUserInfo"),
    path('updateArticle',updateArticle,name="updateArticle"),
    path('getArticleContent',getArticleContent,name="getArticleContent"),
    path('deleteArticle',deleteArticle,name="deleteArticle"),
]
