from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView
from users import views
from rest_framework_simplejwt import views as jwt_views

app_name = "users"

urlpatterns = [
    path("register/", views.UserRegisterationAPIView.as_view(), name="create-user"),
    path("login/", views.UserLoginAPIView.as_view(), name="login-user"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path("logout/", views.UserLogoutAPIView.as_view(), name="logout-user"),
    path("me/", views.UserAPIView.as_view(), name="user-info"),
    path("profile/<int:pk>", views.UserProfileAPIView.as_view(), name="user-profile"),
    path("users/", views.ALLUserProfileAPIView.as_view(), name="user-details"),
    path("userProfile/", views.ProfileUserAPIView.as_view(), name="userProfile-details")
]
