from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
   
    def __str__(self):
        return self.question

class Category(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    cat_name = models.CharField(max_length=100)
    cat_info = models.TextField()
    cat_image = models.ImageField(upload_to='img', blank=True, null=True)
    
    def __str__(self):
        return self.cat_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=16)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    