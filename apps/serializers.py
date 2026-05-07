from rest_framework.fields import SerializerMethodField, ListField, CharField
from rest_framework.serializers import ModelSerializer

from apps.models import Post, Tag, User, Category


class PostModelSerializer(ModelSerializer):
    likes_count = SerializerMethodField()
    is_liked = SerializerMethodField()
    tags = ListField(child=CharField())

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'category', 'tags', 'views_count', 'likes_count', 'is_liked')
        read_only_fields = ('views_count', 'author',)

    def get_likes_count(self, obj: Post):
        return obj.likes_count()

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        tag_list = []
        for tag in tags:
            obj, created = Tag.objects.get_or_create(name=tag)
            tag_list.append(obj)

        instance: Post = super().create(validated_data)
        instance.tags.set(tag_list)
        return instance

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        tag_list = []
        for tag in tags:
            obj, created = Tag.objects.get_or_create(name=tag)
            tag_list.append(obj)

        instance: Post = super().create(validated_data)
        instance.tags.set(tag_list)
        return super().update(instance, validated_data)


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'