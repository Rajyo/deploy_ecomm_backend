from rest_framework import serializers
from .models import Category, Post

class ModalPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','description','image','price']

class CategorySerializer(serializers.ModelSerializer):
    posts = ModalPostSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','category','title','image','posts']

class ModalCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

class PostSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ['id','title','description','image','price','category']
