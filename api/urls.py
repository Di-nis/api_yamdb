from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

# from .views import UserViewSet
from users.views import UserListCreate, UserRetrieveUpdateDestroy
from titles.views import CategoriesViewSet, GenresViewSet, TitlesViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from users.models import User
from users.serializers import UserSerializer

v1_router = DefaultRouter()
v1_router.register('categories', CategoriesViewSet, 'Categories')
v1_router.register('genres', GenresViewSet, 'Genres')
v1_router.register('titles', TitlesViewSet, 'Titles')
# v1_router.register(r'users', UserListCreate, 'Users')

urlpatterns = [
    # path('v1/auth/email/', __, name='____'),
    path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path(r'v1/', include('djoser.urls')),
    path(r'v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
    path('v1/users/', UserListCreate.as_view()),
    # path('v1/users/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list'),
    path("v1/users/<str:username>/", UserRetrieveUpdateDestroy.as_view()),
    # path("v1/users/me/", UserRetrieveUpdateDestroy.as_view()),
]

