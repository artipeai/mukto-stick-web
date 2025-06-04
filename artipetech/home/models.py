

# Create your models here.
# models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    product = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"