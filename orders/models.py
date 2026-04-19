from django.db import models
from menu.models import Product
from django.conf import settings

class orderMan(models.Manager):
    def activ(self):
        return self.get_queryset().filter(complete=False).order_by('Создано в')
    def complete(self):
        return self.get_queryset().filter(complete=True).order_by('Выполнено)')
class order(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Заказы', blank=True)
    create= models.DateTimeField(auto_now_add=True)
    complete= models.BooleanField(default=False)
    objects= orderMan()
    def __str__(self):
        return f'Заказ {self.id} - {"Выполнен" if self.complete else "В процессее"}'

class orderItem(models.Model):
    order= models.ForeignKey(order,on_delete=models.CASCADE,related_name='Вкусности')
    Product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quan= models.PositiveIntegerField(default=1, verbose_name='Скики количество')
