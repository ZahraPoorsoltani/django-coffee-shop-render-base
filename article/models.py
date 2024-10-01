from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name =models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User,models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='article/',default='article/default.jpg')
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('article:article_detail',kwargs={'post_id':self.id})
