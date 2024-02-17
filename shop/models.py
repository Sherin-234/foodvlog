from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    def get_url(self):
        return reverse('prod_cat',args=[self.slug])


class products(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    price=models.IntegerField()
    img=models.ImageField(upload_to='products')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('prod_mod',args=[self.category.slug,self.slug])