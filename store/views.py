from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Slide, Category, CartItem

def store(request):
    categories = Category.objects.all()
    category = request.GET.get('category')
    product_id = request.GET.get('product')
    products = Products.objects.all()
    slides = Slide.objects.all()

    # 🛒 Agar GET orqali product ID kelsa — savatga qo‘shamiz
    if product_id:
        product = get_object_or_404(Products, pk=product_id)
        cart_item = CartItem.objects.filter(customer=request.user, product=product).first()

        if cart_item:
            # Agar mavjud bo‘lsa — miqdorini oshiramiz
            cart_item.quantity += 1
            cart_item.save()
        else:
            # Agar mavjud bo‘lmasa — yangi yaratamiz
            CartItem.objects.create(customer=request.user, product=product, quantity=1)

        return redirect('store:store')

    # 📂 Agar kategoriya tanlangan bo‘lsa — filtrlaymiz
    if category:
        products = Products.objects.filter(category=category)

    return render(request, 'store.html', {
        'products': products,
        'slides': slides,
        'category': category,
        'categories': categories,
    })





def products_detail(requist,slug):
    product = Products.objects.get(slug=slug)
    return render(requist, 'products_detail.html', {'product': product})
    


def cart(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    print([item.total_price() for item in cart_items])
    total_price = sum([item.total_price() for item in cart_items])

    total_quantity = sum([item.quantity for item in cart_items])

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price})