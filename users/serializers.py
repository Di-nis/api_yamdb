from rest_framework import serializers

from .models import User

# from rest_framework.fields import CurrentUserDefault
# from rest_framework.validators import UniqueTogetherValidator



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'lookup_field': 'username'}
        #     # 'url': {'view_name': 'accounts', 'lookup_field': 'account_name'},
        #     'users': {'lookup_field': 'username'}
        # }
        # username = serializers.SlugRelatedField(
        #     read_only=True,
        #     slug_field='username',
        # )