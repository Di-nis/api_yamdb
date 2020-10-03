from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'first_name', 'last_name', 'bio', 'role']


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class EmailCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=100)

