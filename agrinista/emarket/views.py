from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'emarket/home.html')

def login_page(request):
    return render(request, 'emarket/login.html')

def sign_up(request):
    return render(request, 'emarket/signup.html')

def customer_dashboard(request):
    return render(request, 'emarket/customer_dashboard.html')

def seller_dashboard(request):
    return render(request, 'emarket/seller_dashboard.html')

def add_product(request):
    return render(request, 'emarket/add_product.html')

def order_product(request):
    return render(request, 'emarket/order_product.html')


