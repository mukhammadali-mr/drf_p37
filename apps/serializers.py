from rest_framework.serializers import ModelSerializer

from apps.models import Post, Album, Photo, User, Todo, Comment


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PhotoModelSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class AlbumModelSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
