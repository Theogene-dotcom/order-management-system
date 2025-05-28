from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem, Product, User
from .forms import OrderForm


def home(request):
    return render(request, 'app/home.html')

@login_required
def place_order(request):
    if request.user.role != 'customer':
        return redirect('home')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']

            order = Order.objects.create(customer=request.user)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

            return redirect('my_orders')
    else:
        form = OrderForm()

    return render(request, 'app/place_order.html', {'form': form})

@login_required
def my_orders(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'app/my_orders.html', {'orders': orders})

@login_required
def vendor_orders(request):
    if request.user.role != 'vendor':
        return redirect('home')
    orders = Order.objects.prefetch_related('items__product').all().order_by('-date_ordered')
    return render(request, 'app/vendor_orders.html', {'orders': orders})



from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in after sign up
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
