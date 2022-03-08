from distutils.command.upload import upload
from django.db import models
    
class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    
    
    def __str__(self):
        return self.name
    
        
class Image(models.Model):
    category =models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=False,blank=False,)
    description = models.TextField(max_length=500,null=False,blank=False)
    
    def __str__(self):
        return self.description