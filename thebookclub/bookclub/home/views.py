from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import slugify
from .models import Category, Product
from .forms import LendBookForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def lend(request):
    createdby=request.user
    form=LendBookForm(request.POST,request.FILES)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid():
                form.instance.created_by=createdby
                form.instance.slug=slugify(form.instance.title)
                form.save()
                messages.success(request, 'Form submission successful')
                return redirect("borrow/")
        return render(request, 'lend.html', {'form': form})
    else:
        return redirect("users/register")

def all_products(request):
    products = Product.products.all()
    return render(request, 'borrow.html', {'products': products})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'detail.html', {'product': product})