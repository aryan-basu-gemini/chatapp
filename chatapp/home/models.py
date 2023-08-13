from django.db import models

# Create your models here.

class Userdetails(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    
    def _str_(self):
        return self.name
