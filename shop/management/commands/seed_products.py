from django.core.management.base import BaseCommand
from shop.models import Product, Category, Collection, ProductImage
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seed products for the shop'

    def handle(self, *args, **kwargs):
        # Create Categories (Matching by handle to avoid UNIQUE constraints issues)
        cat_lighting, _ = Category.objects.get_or_create(handle='eclairage', defaults={'name': 'Éclairage'})
        cat_protection, _ = Category.objects.get_or_create(handle='protection-electrique', defaults={'name': 'Protection Électrique'})
        cat_industrial, _ = Category.objects.get_or_create(handle='industriel', defaults={'name': 'Industriel'})

        # Create Collection
        col_garoui, _ = Collection.objects.get_or_create(handle='garoui-professional', defaults={'name': 'Garoui Electricity Professional'})

        products_data = [
            {
                'title': 'Dalle LED 600x600 40W 4000K',
                'subtitle': 'Éclairage professionnel haute performance',
                'description': 'Panneau LED professionnel pour bureaux et hôpitaux. Flux lumineux élevé et faible consommation.',
                'sku': 'GAR-LP-40W-600',
                'price': 4500.00,
                'weight': 1200,
                'category': cat_lighting,
                'image_url': 'https://images.unsplash.com/photo-1565814636199-ae8133055c1c?q=80&w=800'
            },
            {
                'title': 'Disjoncteur 1P 16A Courbe C',
                'subtitle': 'Protection modulaire certifiée',
                'description': 'Disjoncteur magnéto-thermique pour la protection des circuits résidentiels et tertiaires.',
                'sku': 'GAR-CB-1P-16A',
                'price': 850.00,
                'weight': 110,
                'category': cat_protection,
                'image_url': 'https://images.unsplash.com/photo-1558444479-2753ada33040?q=80&w=800'
            },
            {
                'title': 'Sonnette Industrielle 250mm 230V',
                'subtitle': 'Alarme sonore forte puissance',
                'description': 'Sonnette industrielle de haute puissance pour zones logistiques et usines.',
                'sku': 'GAR-IB-250',
                'price': 12500.00,
                'weight': 2500,
                'category': cat_industrial,
                'image_url': 'https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=800'
            }
        ]

        for data in products_data:
            handle = slugify(data['title'])
            product, created = Product.objects.update_or_create(
                handle=handle,
                defaults={
                    'title': data['title'],
                    'subtitle': data['subtitle'],
                    'description': data['description'],
                    'sku': data['sku'],
                    'price': data['price'],
                    'weight': data['weight'],
                    'collection': col_garoui,
                    'inventory_quantity': 100,
                }
            )
            product.categories.add(data['category'])
            
            # Add image if not already present
            if not product.images.filter(url=data['image_url']).exists():
                ProductImage.objects.create(product=product, url=data['image_url'])
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created product "{product.title}"'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated product "{product.title}"'))
