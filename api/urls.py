from .views import test,signIn,signUp
from django.urls import path

urlpatterns = [
    path('test', test,name="test"),
    path('signIn', signIn,name="signIn"),
    path('signUp', signUp,name="signUp"),
]
