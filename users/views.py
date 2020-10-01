from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from rest_framework import filters, mixins, permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .models import User
from .permissions import IsAdministrator
from .serializers import EmailCodeSerializer, EmailSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAdministrator, )


class UserRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user


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
