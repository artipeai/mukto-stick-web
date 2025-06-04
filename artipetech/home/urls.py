from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_form, name='contact_form'),
    path('order/', views.order_form, name='order_form'),
]