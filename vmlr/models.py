from django.db import models
from django.contrib.auth.models import User


class Pakets(models.Model):

    class Meta:
        verbose_name_plural = 'пакеты'
        verbose_name = 'пакет'
        
    name = models.CharField(verbose_name='название', max_length=100)
    price = models.CharField(verbose_name='цена', max_length=100)
    image = models.ImageField(upload_to='media/')    
    
    def __str__(self):
        return self.name
    
    
    
class MyPakets(models.Model):
    
    class Meta:
        verbose_name_plural = 'мои пакеты'
        verbose_name = 'мой пакет'
        
    buy = models.ForeignKey('vmlr.Pakets', on_delete=models.PROTECT, related_name='my_paket')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_pakets')
    
    # def __str__(self):
    #     return self

# Create your models here.
