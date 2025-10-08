from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Slide, Category, CartItem

def store(request):
    categories = Category.objects.all()
    category = request.GET.get('categor')
    product_id = request.GET.get('product')
    products = Products.objects.all()
    slides = Slide.objects.all()
    if product_id:
        product = Products.objects.get(pk=product_id)
        cart_item = CartItem.objects.filter(product=product)
        if not cart_item:
            cart_item = CartItem.objects.create(customer=request.user, product=product, quantity=1)
            cart_item.save()
            return redirect('store:store')
        for item in cart_item:
            item.quantity += 1
            item.save()

    products = products.filter(category=category) if category else products
    return render(request, 'store.html', {'products': products, 'slides':slides, 'category':category, 'categories': categories})


def products_detail(requist,slug):
    product = Products.objects.get(slug=slug)
    return render(requist, 'products_detail.html', {'product': product})
    


def cart(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    print([item.total_price() for item in cart_items])
    total_price = sum([item.total_price() for item in cart_items])

    total_quantity = sum([item.quantity for item in cart_items])

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price})



def edit_cart_item(request,pk):
    cart_item = CartItem.objects.get(pk=pk)
    action = request.GET.get('action')

    if action == 'take' and cart_item.quantity > 0:
        if cart_item.quantity == 1:
            cart_item.delete()
            return redirect('store:cart')
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('store:cart')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('store:cart')