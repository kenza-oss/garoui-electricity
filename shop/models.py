from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    handle = models.SlugField(unique=True)
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class")
    
    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='certificates/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=255)
    handle = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255) # Must be exact title as per requirement
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    handle = models.SlugField(unique=True)
    
    # Metadata
    sku = models.CharField(max_length=100, unique=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    
    # Organization
    categories = models.ManyToManyField(Category, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.CharField(max_length=255, blank=True, help_text="Comma separated tags")
    product_type = models.CharField(max_length=255, blank=True)
    
    # Physical Attributes
    weight = models.FloatField(default=0) # in grams
    length = models.FloatField(default=0) # in mm
    height = models.FloatField(default=0) # in mm
    width = models.FloatField(default=0) # in mm
    
    # Technical Specs (Elmark Style)
    ip_rating = models.CharField(max_length=10, blank=True, verbose_name="Indice de protection (IP)")
    material = models.CharField(max_length=100, blank=True)
    wattage = models.CharField(max_length=50, blank=True)
    color_temperature = models.CharField(max_length=50, blank=True)
    warranty_years = models.IntegerField(default=2)
    
    certificates = models.ManyToManyField(Certificate, blank=True)
    technical_pdf = models.FileField(upload_to='products/specs/', blank=True, null=True)
    
    # Inventory
    inventory_quantity = models.IntegerField(default=0)
    manage_inventory = models.BooleanField(default=True)
    
    # Media
    thumbnail = models.ImageField(upload_to='products/thumbnails/', blank=True, null=True)
    
    # Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/gallery/')
    url = models.URLField(blank=True, null=True) # For imported images

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'En attente'),
        ('processing', 'En cours'),
        ('shipped', 'Expédié'),
        ('delivered', 'Livré'),
        ('cancelled', 'Annulé'),
    ])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Customer Info (Simple for now)
    customer_name = models.CharField(max_length=255, blank=True)
    customer_email = models.EmailField(blank=True)
    customer_phone = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"Commande #{self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_title = models.CharField(max_length=255) # Snapshot in case product is deleted
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2) # Snapshot at time of order

    def __str__(self):
        return f"{self.quantity}x {self.product_title}"
