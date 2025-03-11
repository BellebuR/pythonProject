from django.shortcuts import render, redirect
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

def cart_view(request):
    cart_items = CartItem.objects.all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart_view')

@csrf_exempt  # Убедитесь, что вы понимаете безопасность при использовании этого декоратора
def save_order(request):
    if request.method == 'POST':
        order_data = json.loads(request.body)

        # Путь к файлу, в который будут сохраняться заказы
        file_path = 'orders.json'

        # Загружаем существующие заказы
        try:
            with open(file_path, 'r') as file:
                orders = json.load(file)
        except FileNotFoundError:
            orders = []

        # Добавляем новый заказ
        orders.append(order_data)

        # Сохраняем обновленный список заказов
        with open(file_path, 'w') as file:
            json.dump(orders, file, indent=4)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'}, status=400)