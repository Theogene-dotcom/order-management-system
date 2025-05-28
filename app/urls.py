from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('place-order/', views.place_order, name='place_order'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('vendor/orders/', views.vendor_orders, name='vendor_orders'),
    path('signup/', views.signup, name='signup'),
    
]
