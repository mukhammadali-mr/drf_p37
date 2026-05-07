from django_filters import FilterSet

from apps.models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = ['category__id', 'tags__name']
