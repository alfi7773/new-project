from django.db import models

class Pakets(models.Model):

    class Meta:
        verbose_name_plural = 'пакеты'
        verbose_name = 'пакет'
        
    name = models.CharField(verbose_name='название', max_length=100)
    price = models.CharField(verbose_name='цена', max_length=100)
    image = models.ImageField(upload_to='media/')    
    
    def __str__(self):
        return self.name

# Create your models here.
