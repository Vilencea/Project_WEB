from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=67)
    def __str__(self):
        return self.name
    
class activProductMan(models.Manager):
    def imeyetsya(self):
        return self.filter(active=True)
    def halyava(self):
        return self.get_queryset().filter(price__lt=1488)
    
class Product(models.Model):
    name= models.CharField(max_length=67)
    price= models.IntegerField()
    descript= models.TextField()
    Category= models.ForeignKey(Category, on_delete=models.CASCADE , related_name='Товары')
    isActiv= models.BooleanField(default=True, verbose_name='Имееться')
    objects= models.Manager()
    activ= activProductMan()

    def __str__(self):
        return self.name
    

class reviews(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Отзывы')
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)],verbose_name='Рейтинг')

    def __str__(self):
        return f'Отзыв от {self.user.username} для {self.product.name} - Рейтинг: {self.rating}'


