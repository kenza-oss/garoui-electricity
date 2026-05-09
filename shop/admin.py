from django.contrib import admin
from .models import Category, Certificate, Collection, Product, ProductImage, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'handle')
    prepopulated_fields = {'handle': ('name',)}

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'handle')
    prepopulated_fields = {'handle': ('name',)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'price', 'inventory_quantity')
    list_filter = ('collection', 'categories')
    search_fields = ('title', 'sku')
    prepopulated_fields = {'handle': ('title',)}
    inlines = [ProductImageInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'product_title', 'quantity', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at', 'updated_at')
