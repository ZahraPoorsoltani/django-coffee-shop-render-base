from django.db import models
from django.contrib.auth.models import User
from article.models import Category
from django.urls  import reverse
from django.db.models import Avg


# Create your models here.
class Product(models.Model):
    author = models.ForeignKey(User,models.SET_NULL,null=True)
    title_persian = models.CharField(max_length=200)
    title_english = models.CharField(max_length=200,null=True)

    content = models.TextField()
    image = models.ImageField(upload_to='article/',default='article/default.jpg')
    status = models.BooleanField(default=0)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    count_number = models.PositiveSmallIntegerField(default=0)

    
    category = models.ManyToManyField(Category)

    LEVEL_CHOICE = (('LOW','کم'),('MEDIUM','متوسط'),('HIGH','زیاد'))
    caffein_level = models.CharField(max_length=10,
                  choices= LEVEL_CHOICE)

    
    def get_caffein_level_display_name(self):
        for level in self.LEVEL_CHOICE:
            if level[0]==self.caffein_level:
                return level[1]
        return "error"

    material = models.CharField(max_length=200)
    mixed_type = models.CharField(max_length=200)
    weight = models.IntegerField(null=True)
    price = models.PositiveSmallIntegerField()

    def average_rating(self) -> float:
        return Rating.objects.filter(product=self).aggregate(Avg("rating")
                                                          )["rating__avg"] or 0
    

    def __str__(self) -> str:
        return self.title_persian
    
    def get_absolute_url(self):
        return reverse('article:details',kwargs={'post_id':self.id})
    
class Rating(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)



    

class CartItem(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.PositiveSmallIntegerField()
     LEVEL_PAID = (('pending','در انتظار پرداخت'),('paid','پرداخت شده'),('cancel','لغو شده'))
     is_paid = models.CharField(max_length=10, choices= LEVEL_PAID)
     created_date = models.DateTimeField(auto_now_add=True)
     updated_date = models.DateTimeField(auto_now=True)


     @property 
     def total_price(self):
          return int(self.product.price * self.quantity)  

     def __str__(self):
          return self.product.title_persian
     
