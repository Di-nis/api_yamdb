from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
<<<<<<< HEAD


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class EmailCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=32)


=======
        # extra_kwargs = {'lookup_field': 'username'}
        #     # 'url': {'view_name': 'accounts', 'lookup_field': 'account_name'},
        #     'users': {'lookup_field': 'username'}
        # }
        # username = serializers.SlugRelatedField(
        #     read_only=True,
        #     slug_field='username',
        # )
>>>>>>> 64de943176b1007f491320d7631ae4db8ade4ab4
