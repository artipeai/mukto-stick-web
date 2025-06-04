from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Contact, Order
from django.contrib import messages

# Create your views here.

def index(request):
    """
    Render the index page.
    """
    return render(request, 'app/index.html')



def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Your message has been sent successfully!')
    return render(request, 'app/index.html', )

def order_form(request):
    if request.method == 'POST':
        name = request.POST.get('orderName')
        email = request.POST.get('orderEmail')
        phone = request.POST.get('orderPhone')
        whatsapp = request.POST.get('orderWhatsApp')
        address = request.POST.get('orderAddress')
        product = request.POST.get('orderProduct')
        Order.objects.create(
            name=name,
            email=email,
            phone=phone,
            whatsapp=whatsapp,
            address=address,
            product=product
        )
        messages.success(request, 'Your order has been placed successfully!')
        return render(request, 'app/success_order.html', {'success': True})
    
