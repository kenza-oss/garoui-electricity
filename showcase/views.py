import os
from django.conf import settings
from django.shortcuts import render
from partners.models import Partner

def index(request):
    partners = Partner.objects.filter(is_verified=True).order_by('-created_at')
    
    # Lecture des images du terrain
    field_images_dir = os.path.join(settings.MEDIA_ROOT, 'field_images')
    field_images = []
    if os.path.exists(field_images_dir):
        field_images = [f for f in os.listdir(field_images_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    return render(request, 'showcase/index.html', {
        'partners': partners,
        'field_images': field_images
    })

def certificates(request):
    return render(request, 'showcase/certificates.html')

def resources(request):
    return render(request, 'showcase/resources.html')

def about(request):
    return render(request, 'showcase/about.html')
