from django.db import models

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
