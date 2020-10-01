from django.urls import include, path
from rest_framework.routers import DefaultRouter

from titles.views import CategoriesViewSet, GenresViewSet, TitlesViewSet
from users.views import UserRetrieveUpdate, UserViewSet, get_token, send_code

v1_router = DefaultRouter()

v1_router.register('categories', CategoriesViewSet, 'Categories')
v1_router.register('genres', GenresViewSet, 'Genres')
v1_router.register('titles', TitlesViewSet, 'Titles')
v1_router.register('users', UserViewSet, 'Users')

urlpatterns = [
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/auth/email/', send_code, name='register'),
    path("v1/users/me/", UserRetrieveUpdate.as_view()),
    path('v1/', include(v1_router.urls)),
]
