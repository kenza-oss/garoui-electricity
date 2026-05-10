import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectCategory

def project_list(request):
    category_handle = request.GET.get('category', '')
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()

    if category_handle:
        projects = projects.filter(category__handle=category_handle)

    featured = projects.filter(featured=True)[:3]

    # Lecture des images du terrain (dans static pour Render)
    field_images_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'field_images')
    field_images = []
    if os.path.exists(field_images_dir):
        field_images = [f for f in os.listdir(field_images_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    return render(request, 'projects/project_list.html', {
        'projects': projects,
        'categories': categories,
        'active_category': category_handle,
        'featured': featured,
        'field_images': field_images,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    other_projects = Project.objects.exclude(pk=project.pk).order_by('-year')[:3]
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'other_projects': other_projects,
    })
