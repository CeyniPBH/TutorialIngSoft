from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django import forms 

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

class Product:
    products = [
        {'id': 1, 'name': 'TV', 'description': 'Best TV'},
        {"id":"2", "name":"iPhone", "description":"Best iPhone"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses"}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):  # Este método debe estar indentado dentro de la clase
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

def get(self, request, id):
    viewData = {}
    product = Product.products[int(id)-1]
    viewData["title"] = product["name"] + " - Online Store"
    viewData["subtitle"] = product["name"] + " - Product information"
    viewData["product"] = product

    return render(request, self.template_name, viewData)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Product Name')
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create Product - Online Store"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # For example, save the product to the database
            return redirect('form')  # Redirect to the product index page
        else:
            viewData = {}
            viewData["title"] = "Create Product - Online Store"
            viewData["form"] = form
            return render(request, self.template_name, viewData)