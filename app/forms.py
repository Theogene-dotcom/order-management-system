from django import forms
from .models import OrderItem, Product

from django import forms
from .models import Product

class OrderForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label="Select Product")
    quantity = forms.IntegerField(min_value=1, label="Quantity")



from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']

