from django.urls import path

from apps.views import PostListAPIView, UserListAPIView, CommentListAPIView, AlbumListAPIView, TodoListAPIView, \
    PhotoListAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('comments/', CommentListAPIView.as_view()),
    path('albums/', AlbumListAPIView.as_view()),
    path('todos/', TodoListAPIView.as_view()),
    path('photos/', PhotoListAPIView.as_view()),

]
