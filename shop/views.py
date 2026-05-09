import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Order, OrderItem, Category

def product_list(request):
    query = request.GET.get('q')
    category_handle = request.GET.get('category')
    
    products = Product.objects.all()
    
    if query:
        products = products.filter(title__icontains=query)
    
    if category_handle:
        products = products.filter(categories__handle=category_handle)
    
    categories = Category.objects.all()
    total_count = Product.objects.count()
    
    return render(request, 'shop/product_list.html', {
        'products': products,
        'categories': categories,
        'total_count': total_count
    })

def product_detail(request, handle):
    product = get_object_or_404(Product, handle=handle)
    return render(request, 'shop/product_detail.html', {'product': product})

def cart(request):
    return render(request, 'shop/cart.html')

@csrf_exempt
def place_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart = data.get('cart', [])
            
            if not cart:
                return JsonResponse({'status': 'error', 'message': 'Le panier est vide'}, status=400)
            
            # Create Order
            order = Order.objects.create(
                customer_name="Client Web", # Could be extended with a form
                total_price=0 # Will be calculated below
            )
            
            total = 0
            for item in cart:
                try:
                    product = Product.objects.get(title=item['title'])
                    price = product.price
                    quantity = int(item['quantity'])
                    
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        product_title=product.title,
                        quantity=quantity,
                        price=price
                    )
                    total += price * quantity
                except Product.DoesNotExist:
                    continue
            
            order.total_price = total
            order.save()
            
            return JsonResponse({'status': 'success', 'order_id': order.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=405)
