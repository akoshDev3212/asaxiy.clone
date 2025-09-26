from django.shortcuts import render
from .models import Products, Slide


def store(request):
    products = Products.objects.all()
    slides = Slide.objects.all()
    return render(request, 'store.html', {'products': products, 'slides': slides})



def products_detail(requist,slug):
    product = Products.objects.get(slug=slug)
    return render(requist, 'produc_detail.html', {'product': product})
    
