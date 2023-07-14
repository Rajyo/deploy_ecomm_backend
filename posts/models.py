from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.SmallAutoField(auto_created=True, primary_key=True, blank=False, null=False)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='category', blank=True, null=True)

    def __str__(self):
        return self.category
    

class Post(models.Model):
    id = models.SmallAutoField(auto_created=True, primary_key=True, blank=False, null=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='post', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title