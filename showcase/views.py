import os
from django.conf import settings
from django.shortcuts import render
from partners.models import Partner

def index(request):
    partners = Partner.objects.filter(is_verified=True).order_by('-created_at')
    
    # Lecture des images du terrain (dans static pour Render)
    field_images_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'field_images')
    field_images = []
    if os.path.exists(field_images_dir):
        field_images = [f for f in os.listdir(field_images_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    return render(request, 'showcase/index.html', {
        'partners': partners,
        'field_images': field_images
    })


def about(request):
    return render(request, 'showcase/about.html')

