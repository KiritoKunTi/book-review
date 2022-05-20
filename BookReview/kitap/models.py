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
    cat_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    
    
    def __str__(self):
        return self.cat_name

class Book(models.Model):
    book_id = models.BigAutoField(primary_key=True)
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_info = models.TextField()
    book_image = models.ImageField(upload_to='img', blank=True, null=True)
    book_publisher = models.CharField(max_length=100)
    book_rating = models.DecimalField(decimal_places=1, max_digits=2)
    book_slug = models.SlugField()
    book_cat = models.ForeignKey(Category, related_name='books', on_delete=models.DO_NOTHING)
    book_pages = models.IntegerField()
    
    
    def __str__(self):
        return self.book_title

