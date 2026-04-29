from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('customer/', views.customer_dashboard, name='customer'),
    path('seller/', views.seller_dashboard, name='seller'),
    path('addp/', views.add_product, name='addp'),
    path('orderp/', views.order_product, name='orderp'),
]