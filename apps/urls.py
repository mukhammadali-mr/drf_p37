from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from apps.views import PostModelViewSet, UserListCreateAPIView

router = SimpleRouter(trailing_slash=False)
router.register('posts', PostModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users', UserListCreateAPIView.as_view(), name='user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

]
