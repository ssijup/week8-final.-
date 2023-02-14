from django.db import models

# Create your models here.
class Userdetails(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=50)
    u_active = models.BooleanField(default=True)
    def __str__(self): 
        return self.user_name 



class Category(models.Model):
    cate_name = models.CharField(max_length=100)
    def __str__(self): 
        return self.cate_name 

class Products(models.Model):
    book_title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='newimg')
    p_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    def __str__(self): 
        return self.p_category 


    

