from django.contrib import admin
from .models import Product, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')  # Campos visibles en la lista
    search_fields = ('name',)  # Campo de búsqueda
    list_filter = ('created_at', 'updated_at')  # Filtros laterales

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'description')  # Campos visibles en la lista
    search_fields = ('description',)  # Campo de búsqueda
    list_filter = ('product',)  # Filtro lateral por producto