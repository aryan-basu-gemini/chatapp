from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
      path("",views.home,name='home'),
      path("index",views.index,name='index'),
      path("signup",views.signup,name='signup'),
      path("message/<int:id>",views.message,name='message')
]