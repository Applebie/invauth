from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        exclude = ['password',]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'first_name', 'last_name',]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model()(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user

##############33
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.state import token_backend

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data['access'], verify=True)
        user_uid=decoded_payload['user_id']
        # add filter query
        data.update({'custom_field': user_uid})
        return data

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         # The default result (access/refresh tokens)
#         data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
#         # Custom data you want to include
#         data.update({'user': self.user.username})
#         data.update({'id': self.user.id})
#         # and everything else you want to send in the response
#         return data

# from rest_framework import serializers
# from django.contrib.auth import get_user_model # If used custom user model


# UserModel = get_user_model()


# class UserSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(write_only=True)

#     def create(self, validated_data):

#         user = UserModel.objects.create_user(
#             username=validated_data['username'],
#             password=validated_data['password'],
#         )

#         return user

#     class Meta:
#         model = UserModel
#         # Tuple of serialized model fields (see link [2])
#         fields = ( "id", "username", "password", )



# from allauth.account import app_settings as allauth_settings
# from allauth.utils import email_address_exists
# from allauth.account.adapter import get_adapter
# from allauth.account.utils import setup_user_email
# from rest_framework import serializers

# class RegisterSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
#     first_name = serializers.CharField(required=True, write_only=True)
#     last_name = serializers.CharField(required=True, write_only=True)
#     password1 = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)

#     def validate_email(self, email):
#         email = get_adapter().clean_email(email)
#         if allauth_settings.UNIQUE_EMAIL:
#             if email and email_address_exists(email):
#                 raise serializers.ValidationError(
#                     _("A user is already registered with this e-mail address."))
#         return email

#     def validate_password1(self, password):
#         return get_adapter().clean_password(password)

#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError(
#                 _("The two password fields didn't match."))
#         return data

#     def get_cleaned_data(self):
#         return {
#             'first_name': self.validated_data.get('first_name', ''),
#             'last_name': self.validated_data.get('last_name', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', ''),
#         }

#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         adapter.save_user(request, user, self)
#         setup_user_email(request, user, [])
#         user.save()
#         return user


# from rest_framework import serializers
# from rest_auth.registration.serializers import RegisterSerializer
# from .models import UserProfile



# class RegistrationSerializer(RegisterSerializer):

#     first_name = serializers.CharField(required=False)
#     last_name = serializers.CharField(required=False)
#     #personal_id = serializers.CharField(required=True)

#     def custom_signup(self, request, user):
#         user.first_name = self.validated_data.get('first_name', '')
#         user.last_name = self.validated_data.get('last_name', '')
#         # user.userprofile.personal_id = self.validated_data.get(
#         #     'personal_id', '')

#         user.save(update_fields=['first_name', 'last_name'])
#         #user.userprofile.save(update_fields=['org_id'])