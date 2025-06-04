

# Register your models here.
from django.contrib import admin
from .models import Contact, Order

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    date_hierarchy = 'created_at'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'product', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('name', 'email', 'phone', 'address', 'product')
    date_hierarchy = 'created_at'