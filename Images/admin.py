from django.contrib import admin

# Register your models here.
from .models import Category, Image

admin.site.register(Category)
admin.site.register(Image)