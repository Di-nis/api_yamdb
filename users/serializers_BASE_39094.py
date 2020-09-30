from rest_framework import serializers

from .models import User

# from rest_framework.fields import CurrentUserDefault
# from rest_framework.validators import UniqueTogetherValidator



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'