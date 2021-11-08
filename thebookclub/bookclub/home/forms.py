from django.forms import ModelForm
from django import forms
from .models import Product,Category

class LendBookForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        exclude=['is_active','in_stock','created_by','slug']