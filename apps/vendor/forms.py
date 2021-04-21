from django.forms import ModelForm
from apps.product.models import Product


class ProductForm(ModelForm):
    model = Product
    fields = ['category', 'image', 'title', 'description', 'price']
