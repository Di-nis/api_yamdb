from django.urls import include, path
from rest_framework.routers import DefaultRouter

from titles.views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                          ReviewViewSet, TitlesViewSet)
from users.views import UserViewSet, get_token, send_code

v1_router = DefaultRouter()
v1_router.register('categories', CategoriesViewSet, 'Categories')
v1_router.register('genres', GenresViewSet, 'Genres')
v1_router.register('titles', TitlesViewSet, 'Titles')
v1_router.register('users', UserViewSet, 'Users')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, 'Review')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, 'Comment')


extra_patterns = [
    path('token/', get_token, name='get_token'),
    path('email/', send_code, name='register'),
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include(extra_patterns)),
]
