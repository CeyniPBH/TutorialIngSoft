from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class homePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
    "title": "About us - Online Store",
    "subtitle": "About us",
    "description": "This is an about page ...",
    "author": "Developed by: Your Name",
})
    
class ContactPageView(TemplateView):
    template_name = 'pages/about.html'
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
    "title": "Contact us - Online Store",
    "subtitle": "COntact us",
    "email": "pepito123@gmail.com",
    "address": "Cra 40 # 22-08",
    "phone": "1234567890",
})