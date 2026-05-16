from django.core.management.base import BaseCommand
from shop.models import Product, Category, Collection
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seed products for the shop'

    def handle(self, *args, **kwargs):
        # Create Categories
        cat_lighting, _ = Category.objects.get_or_create(name='Éclairage', handle='eclairage')
        cat_protection, _ = Category.objects.get_or_create(name='Protection Électrique', handle='protection-electrique')
        cat_industrial, _ = Category.objects.get_or_create(name='Industriel', handle='industriel')

        # Create Collection
        col_Garoui Electricity, _ = Collection.objects.get_or_create(name='Garoui Electricity Professional', handle='Garoui Electricity-professional')

        products_data = [
            {
                'title': 'LED PANEL 600x600 40W 4000K',
                'subtitle': 'Dalle LED haute performance',
                'description': 'Panneau LED professionnel pour bureaux et hôpitaux. Flux lumineux élevé et faible consommation.',
                'sku': 'ELM-LP-40W-600',
                'price': 4500.00,
                'weight': 1200,
                'category': cat_lighting,
                'thumbnail_url': 'https://www.Garoui Electricityholding.eu/uploads/products/12345/thumb.jpg'
            },
            {
                'title': 'CIRCUIT BREAKER 1P 16A C-CURVE',
                'subtitle': 'Disjoncteur divisionnaire',
                'description': 'Disjoncteur magnéto-thermique pour la protection des circuits résidentiels et tertiaires.',
                'sku': 'ELM-CB-1P-16A',
                'price': 850.00,
                'weight': 110,
                'category': cat_protection,
                'thumbnail_url': 'https://www.Garoui Electricityholding.eu/uploads/products/67890/thumb.jpg'
            },
            {
                'title': 'INDUSTRIAL BELL 250mm 230V',
                'subtitle': 'Alarme sonore industrielle',
                'description': 'Sonnette industrielle de haute puissance pour zones logistiques et usines.',
                'sku': 'ELM-IB-250',
                'price': 12500.00,
                'weight': 2500,
                'category': cat_industrial,
                'thumbnail_url': 'https://www.Garoui Electricityholding.eu/uploads/products/11223/thumb.jpg'
            }
        ]

        for data in products_data:
            product, created = Product.objects.get_or_create(
                title=data['title'],
                defaults={
                    'subtitle': data['subtitle'],
                    'description': data['description'],
                    'handle': slugify(data['title']),
                    'sku': data['sku'],
                    'price': data['price'],
                    'weight': data['weight'],
                    'collection': col_Garoui Electricity,
                    'inventory_quantity': 100
                }
            )
            if created:
                product.categories.add(data['category'])
                self.stdout.write(self.style.SUCCESS(f'Successfully created product "{product.title}"'))
            else:
                self.stdout.write(self.style.WARNING(f'Product "{product.title}" already exists'))
