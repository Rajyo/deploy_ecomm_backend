from .views import PostViewSet, CategoryViewSet, CreatePostAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = "post"

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'createPost', CreatePostAPIView, basename='create_post')

list_category = CategoryViewSet.as_view({'get':'list'})
retrieve_category = CategoryViewSet.as_view({'get':'retrieve'})

urlpatterns = [
    path('category/', list_category, name='list-category'),
    path('category/<str:category>/', retrieve_category, name='retrieve-category'),
    path('', include(router.urls))
]