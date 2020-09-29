from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

# from .views import UserViewSet
from users.views import UserListCreate
from titles.views import CategoriesViewSet, GenresViewSet, TitlesViewSet

v1_router = DefaultRouter()
v1_router.register('categories', CategoriesViewSet, 'Categories')
v1_router.register('genres', GenresViewSet, 'Genres')
v1_router.register('titles', TitlesViewSet, 'Titles')
v1_router.register(r'users', UserListCreate)

urlpatterns = [
    # path('v1/auth/email/', __, name='____'),
    path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path(r'v1/', include('djoser.urls')),
    path(r'v1/', include('djoser.urls.jwt')),
    # path('v1/users/', UserViewSet),
    # path('v1/users/', UserList),
    path('v1/', include(v1_router.urls)),
    path("users/<str:username>/", UserListCreate),
]

