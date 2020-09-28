from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

# from .views import UserViewSet
from users.views import UserList

router_v1 = DefaultRouter()
# router_v1.register(r'users', UserList)

urlpatterns = [
    # path('v1/auth/email/', __, name='____'),
    path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('djoser.urls')),
    # path(r'auth/', include('djoser.urls.jwt')),
    # path('v1/users/', UserViewSet),
    # path('v1/users/', UserList),
    path('v1/', include(router_v1.urls)),
]