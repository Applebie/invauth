from .models import User
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,UserDetailSerializer,CustomTokenRefreshSerializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from decouple import config
from django.http import JsonResponse
import json

class UserList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class HelloView(APIView):
    #permission_classes = (IsAuthenticated,)
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        token_user_email = request.user.email
        token_user_id = request.user.id
        data = User.objects.get(pk=token_user_id)
        #import pdb; pdb.set_trace()
        serialzeddata = UserDetailSerializer(data)
        return JsonResponse(serialzeddata.data)

        #queryset = User.objects.filter(username=token_user_username).values()
        # return JsonResponse({"data": list(queryset)})
        # token_user_username = request.user.username
        # queryset = User.objects.filter(username=token_user_username).values()
        
        #return(queryset)




from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



###

from rest_framework_simplejwt.views import TokenRefreshView
class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom Refresh token View
    """
    serializer_class = CustomTokenRefreshSerializer
#### GetUserProfile **********************88

from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
from .models import User # just import your model here
import jwt


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request): # it will return user object
        try:#if(verify_token_response.status_code == 200):
            jwt_object      = JWTAuthentication() 
            header          = jwt_object.get_header(request)
            raw_token       = jwt_object.get_raw_token(header)
            validated_token = jwt_object.get_validated_token(raw_token)
            user            = jwt_object.get_user(validated_token)
            print(user)
            print(request)
            # token = get_authorization_header(request).decode('utf-8')
            #token = jwt.decode(validated_token, config('app_secret_key'), algorithms=["HS256"])
            if token is None or token == "null" or token.strip() == "":
                raise exceptions.AuthenticationFailed('Authorization Header or Token is missing on Request Headers')
            print(token)
            #decoded = jwt.decode(token, config('app_secret_key')) # settings.SECRET_KEY)
            #username = decoded['username']
            #user_obj = User.objects.get(username=username)
        except jwt.ExpiredSignature :
            raise exceptions.AuthenticationFailed('Token Expired, Please Login')
        except jwt.DecodeError :
            raise exceptions.AuthenticationFailed('Token Modified by thirdparty')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid Token')
        except Exception as e:
            raise exceptions.AuthenticationFailed(e)
        return (user_obj, None)

    def get_user(self, userid):
        try:
            return User.objects.get(pk=userid)
        except Exception as e:
            return None



######**********************************8

## Get UserToken override

# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from decouple import config
# from django.contrib.auth import authenticate
# import jwt




# @api_view(['POST'])
# @permission_classes([AllowAny])
# def get_tokens_for_user(request):

#     # username = request.POST.get("username")
#     # password = request.POST.get("password")

#     # user = authenticate(username=username, password=password);

#     if user is not None:

#         #refreshToken = RefreshToken.for_user(user)
#         #accessToken = refreshToken.access_token
        
#         accessToken = request.access_token
#         decodeJTW = jwt.decode(str(accessToken), config('app_secret_key'), algorithms=["HS256"]);

#         # add payload here!!
#         decodeJTW['iat'] = '1590917498'
#         decodeJTW['user'] = 'tiago'
#         decodeJTW['date'] = '2020-05-31'

#         #encode
#         encoded = jwt.encode(decodeJTW, config('SECRET_KEY'), algorithm="HS256")
    
#         return Response({
#             'status': True,
#             'refresh': str(refreshToken),
#             'access': str(encoded),
#         })

#     else:
#         return Response({
#             'status': False
#         })
#         # No backend authenticated the credentials

