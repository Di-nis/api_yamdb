from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from users import views

from .views import UserListCreate

router = DefaultRouter()  
router.register(r'users', UserListCreate, basename='users') 

urlpatterns = [ 
    path('auth/email/', views.send_code),
    path('auth/token/', views.get_token), 
]

urlpatterns += [
    path('v1/', include(router.urls)),
]