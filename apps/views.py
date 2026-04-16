from rest_framework.generics import ListAPIView

from apps.models import Post, User, Comment, Todo, Album, Photo
from apps.serializers import AlbumModelSerializer, PhotoModelSerializer, UserModelSerializer, \
    CommentModelSerializer, TodoModelSerializer, PostModelSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer


class TodoListAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


class AlbumListAPIView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer


class PhotoListAPIView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoModelSerializer
