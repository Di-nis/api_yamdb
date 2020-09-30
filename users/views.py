from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import filters, mixins, viewsets, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    # lookup_value_regex = '[0-9a-f]{32}'
    permission_classes = (IsAdminUser, )

    # @action(detail=False)
    # def me(self, request, pk=None):
    #     """
    #     Returns a list of all the group names that the given
    #     user belongs to.
    #     """
    #     user = self.request.user
    #     return Response(user.id)
        # return Response([group.name for group in groups])

    # def get_object(self):
    #     return self.request.user
from .permissions import IsAdministrator
from .serializers import EmailCodeSerializer, EmailSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
# from rest_framework.decorators import action


@api_view(['POST'])
def send_code(request):
    serializer = EmailSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data['email']
        if not User.objects.filter(email=email):
            user=User.objects.create_user(email=email)
        else:
            user=User.objects.get(email=email) 
        confirmation_code = PasswordResetTokenGenerator().make_token(user)
        send_mail(
        'Confirmation code',
        confirmation_code,
        'yamdb@example.com',
        [email],
        fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def get_token(request):
    serializer = EmailCodeSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data['email']
        confirmation_code = serializer.data['confirmation_code']
        user=User.objects.get(email=email)
        if PasswordResetTokenGenerator().check_token(user, confirmation_code):
            token = AccessToken.for_user(user)
            return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserViewSet(viewsets.ModelViewSet):
# @action(detail=True, methods=['post'])
# class UserViewSet(ListAPIView):


# # class UserListCreate(viewsets.ModelViewSet):
# # @api_view(['GET', 'POST'])
# # @action(methods=['post'], detail=True)
# class UserListCreate(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser, )
#     # permission_classes = (IsAuthenticated, )
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['username']
#     search_fields = ['username', ]
#     # pagination_class = PageNumberPagination
#     # pagination_class = LimitOffsetPagination

#     # def list(self, request):
#     #     # Note the use of `get_queryset()` instead of `self.queryset`
#     #     queryset = self.get_queryset()
#     #     serializer = UserSerializer(queryset, many=True)
#     #     return Response(serializer.data)


# class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     # user = User.objects.get(username=username)
#     serializer_class = UserSerializer
#     # permission_classes = (IsAdminUser, )
#     # permission_classes = (IsAuthenticated, )
#     lookup_field = ('username')
#     lookup_url_kwarg = ('username')

#     # def get_object(self):
#     #     lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
#     #     filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
#     #     return get_object_or_404(User, **filter_kwargs)

#     # def get_object(self):
#     #     queryset = self.get_queryset()
#     #     filter = {}
#     #     for field in self.multiple_lookup_fields:
#     #         filter[field] = self.kwargs[field]

#     #     obj = get_object_or_404(queryset, **filter)
#     #     self.check_object_permissions(self.request, obj)
#     #     return obj


# # # class UserRetrieve(RetrieveAPIView):
class UserRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    # user = User.objects.get(username=username)
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    # lookup_field = ('username')

    def get_object(self):
        return self.request.user



# # class UserRetrieveUpdate(viewsets.ModelViewSet):
# #     """
# #     A viewset for viewing and editing user instances.
# #     """
# #     serializer_class = UserSerializer
# #     # User = get_user_model()
# #     queryset = User.objects.all()
# #     # filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
# #     # filter_fields = ('username', 'email', 'usertype')
# #     # search_fields = ('username', 'email', 'usertype')

# #     # @list_route(permission_classes=[IsAuthenticated])
# #     def me(self, request, *args, **kwargs):
# #         # User = get_user_model()
# #         self.object = get_object_or_404(User, pk=request.user.id)
# #         serializer = self.get_serializer(self.object)
# #         return Response(serializer.data)



#     # username пользователь для фильтрации, поиск по части username
# class UserListCreate(viewsets.ModelViewSet):
# @api_view(['GET', 'POST'])
# @action(methods=['post'], detail=True)
class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['username']
    search_fields = ['username', ]
    permission_classes = [IsAdministrator,]


    @action(detail=False, methods=['get', 'patch'], permission_classes = [IsAuthenticated])
    def me(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
