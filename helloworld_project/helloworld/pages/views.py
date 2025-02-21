from django.views import View

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV"},
        {"id":"2", "name":"iPhone", "description":"Best iPhone"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses"}
]
class ProductIndexView(View):
    template_name = 'products/index.html'


def get(self, request):
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