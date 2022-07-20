""" urls file for posts app """
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'posts'

urlpatterns = [
    path('users/', views.UserList.as_view(), name='users_list'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view(), name='posts_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
