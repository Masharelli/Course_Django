from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length = 200)
    direction = models.CharField(max_length = 200) 
    email = models.EmailField()
    tel = models.CharField(max_length = 200)

class Articles(models.Model):
    name_article = models.CharField(max_length = 200)    
    sections = models.CharField(max_length = 200)    
    price = models.IntegerField()

class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()        