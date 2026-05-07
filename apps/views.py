from django.db.models import Exists, OuterRef, Value, BooleanField
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.filters import PostFilter
from apps.models import Post, Like, User
from apps.serializers import PostModelSerializer, UserModelSerializer


@extend_schema(tags=["Users"])
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=["Posts"])
class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    http_method_names = ['get', 'post', 'patch']
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    filterset_class = PostFilter
    ordering_field = 'created_at', 'views_count'
    search_fields = ['title', 'content']

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        if user.is_authenticated:
            key = Exists(Like.objects.filter(post_id=OuterRef('pk'), user=user))
        else:
            key = Value(False, BooleanField())

        return qs.annotate(
            likes_count=Count('likes'),
            is_liked=key
        )

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [AllowAny()]

        if self.request.method == 'POST':
            return [IsAuthenticated()]

        if self.request.method in ['PUT', 'PATCH']:
            return [IsAuthenticated(), IsAdminUser()]

        if self.request.method == 'DELETE':
            return [IsAdminUser()]

        return super().get_permissions()

    @action(detail=True, methods=['post'], url_path='like', serializer_class=None)
    def set_like(self, request, pk=None):
        return Response({'status': 'password set'})

    @action(detail=True, methods=['post'], url_path='unlike', serializer_class=None)
    def set_unlike(self, request, pk=None):
        Like.objects.get_or_create(user=request.user, post=pk)
        return Response({'status': 'ok'})
