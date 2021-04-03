from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('main/', views.mainpage),
    path('news/', views.newslist),
    path('navigation/', views.navigation),
    path('livechat/', views.livechat),
    path('sendmes/', views.sendmessage),
    path(r'news/<id2>/', views.seenews),
    path('register/', views.register)
]