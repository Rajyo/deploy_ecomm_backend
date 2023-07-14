from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile
from .serializers import *
from rest_framework.views import APIView

# Create your views here.

class UserRegisterationAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserLoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = CustomUserSerializer(user)
        data = serializer.data
        data["tokens"] = get_tokens_for_user(user)
        return Response(data, status=status.HTTP_200_OK)



class UserLogoutAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh_token"]
            print(refresh_token)
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response(
                {'data': "Succesfully Logged Out"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserAPIView(RetrieveUpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class ProfileUserAPIView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileUserSerializer
    paginator = None

    def get_object(self):
        return self.request.user



class UserProfileAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)


class ALLUserProfileAPIView(ListAPIView):
    model = Profile
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (AllowAny,)
    paginator = None




