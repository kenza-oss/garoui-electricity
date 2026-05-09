from django.shortcuts import render
from shop.models import Product
from partners.models import Partner

def overview(request):
    total_products = Product.objects.count()
    low_stock = Product.objects.filter(inventory_quantity__lt=5).count()
    try:
        total_partners = Partner.objects.count()
    except:
        total_partners = 0
    context = {
        'total_products': total_products,
        'low_stock': low_stock,
        'total_partners': total_partners,
    }
    return render(request, 'dashboard/overview.html', context)

def products(request):
    products = Product.objects.all().select_related('collection').prefetch_related('categories')
    return render(request, 'dashboard/products.html', {'products': products})

def orders(request):
    return render(request, 'dashboard/orders.html')

def inventory(request):
    products = Product.objects.all().order_by('inventory_quantity')
    return render(request, 'dashboard/inventory.html', {'products': products})

def customers(request):
    try:
        partners = Partner.objects.all()
    except:
        partners = []
    return render(request, 'dashboard/customers.html', {'partners': partners})

def settings_view(request):
    return render(request, 'dashboard/settings.html')
