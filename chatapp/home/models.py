from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Userdetails(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    
    def _str_(self):
        return self.name

class Chat(models.Model):
    from_message = models.CharField(max_length=40)
    message = ArrayField(models.CharField(max_length=1000))
    to_message = models.CharField(max_length=40)