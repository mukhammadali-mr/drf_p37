from django.contrib import admin

from apps.models import Post, User, Comment, Album, Photo, Todo


# Register your models here.


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Todo)
class TodoModelAdmin(admin.ModelAdmin):
    pass
