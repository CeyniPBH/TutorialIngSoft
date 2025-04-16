from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms 
from django.core.exceptions import ValidationError 
from .models import Product 

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'About Us - Online Store',
            'subtitle': 'About us',
            'description': 'This is the about page of our website.',
            'keywords': 'about, website, information',
        })
        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Contact Us - Online Store',
            'subtitle': 'Contact us',
            'description': 'This is the contact page of our website.',
            'keywords': 'contact, website, information',
        })
        return context

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Productos - Tienda Online"
        viewData["subtitle"] = "Lista de productos"
        viewData["products"] = Product.objects.all()  
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            product_id = int(id)
            if product_id < 1:
                raise ValueError("El ID del producto debe ser 1 o mayor")
            product = get_object_or_404(Product, pk=product_id)
        except (ValueError, IndexError):
            return HttpResponseRedirect(reverse('home'))

        viewData = {}
        product = get_object_or_404(Product, pk=product_id)
        viewData["title"] = product.name + " - Tienda Online"
        viewData["subtitle"] = product.name + " - Información del producto"
        viewData["product"] = product
        return render(request, self.template_name, viewData)
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError('El precio no puede ser negativo.')
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Crear Producto - Tienda Online"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-created')
        else:
            viewData = {}
            viewData["title"] = "Crear Producto - Tienda Online"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

class ProductListView(ListView):
    model = Product
    template_name = 'list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Productos - Tienda Online'
        context['subtitle'] = 'Lista de productos'
        return context
    
class CartView(View):
    template_name = 'cart/index.html'

    def get(self, request):
        products = {}
        products[121] = {'name': 'Tv samgsung', 'price': '1000'}
        products[11] = {'name': 'Iphone', 'price': '2000'}
        
        cart_products = {}
        cart_product_data = request.session.get('cart_product_data', {})

        for key, product in products.items():
            if str(key) in cart_product_data.keys():
                cart_products[key] = product
        
        viewData = {
            'title': 'Carrito de Compras - Tienda Online',
            'subtitle': 'Carrito de compras',
            'products': products,
            'cart_products': cart_products
        }

        return render(request, self.template_name, viewData)

    def post(self, request, product_id):
        # Obtener los productos del carrito desde la sesión y agregar el nuevo producto
        cart_product_data = request.session.get('cart_product_data', {})
        cart_product_data[product_id] = product_id

        request.session['cart_product_data'] = cart_product_data

        return redirect('cart_index')

class CartRemoveAllView(View):
    def post(self, request):
        # Eliminar todos los productos del carrito en la sesión
        if 'cart_product_data' in request.session:
            del request.session['cart_product_data']

        return redirect('cart_index')