from django.contrib import admin

# Register your models here.
from .models import Book, Product

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')

admin.site.register(Book) 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','price','description')
    search_fields = ('name', 'description','price')

admin.site.register(Product)