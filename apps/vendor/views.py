from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Vendor
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from apps.product.models import Product
from .forms import ProductForm


def vendor_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)

            vendor = Vendor.objects.create(name=user.username, created_by=user)
            return redirect('home')
        else:
            form = UserCreationForm()

    return render(request, 'vendor/sign_up.html', {'form': form})


@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()

    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor, 'producst': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('admin_login')

        else:
            form = ProductForm()

        return render(request, 'vendor/add_product.html', {'form': form})