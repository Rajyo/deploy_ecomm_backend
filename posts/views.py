# Create your views here.
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    queryset = Post.objects.order_by('-date')
    serializer_class = PostSerializer
    paginator = None


class CreatePostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    queryset = Post.objects.order_by('-date')
    serializer_class = PostSerializer
    paginator = None

    def perform_create(self, serializer):
        post = serializer.save()
        print(post)
        try:
            cate = self.request.data['category']
            print(type(cate))
        except:
            cate = ""        
        if cate:
            category = Category.objects.get(category=cate)
            print(type(category))
            print(category)
            post.category = category
        else:
            print("wrong category")
        
        post.save()
    

class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True, context={'request': request})
        paginator = None
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        category = kwargs.get('category',None)
        category = Category.objects.get(category=category)
        serializer = CategorySerializer(category, context={'request': request})
        paginator = None
        return Response(serializer.data)
    
