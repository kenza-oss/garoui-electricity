import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectCategory, SonelgazMissionImage

MISSION_CATEGORIES = [
    {
        'key': 'coupure',
        'label': 'Coupure',
        'icon': 'fas fa-power-off',
        'color': '#ef4444',
        'description': "Sur ordre de Sonelgaz, les équipes de Garoui Electricity effectuent des coupures de courant chez les abonnés ayant des impayés de consommation. Cette mission administrative et technique vise à régulariser la situation des abonnés défaillants et à assurer l'équité dans la gestion du réseau.",
        'challenge': "Intervenir avec professionnalisme et dans le strict respect des procédures Sonelgaz, en localisant précisément le compteur de l'abonné concerné, même dans des immeubles complexes ou des zones difficiles d'accès.",
    },
    {
        'key': 'retablissement',
        'label': 'Rétablissement',
        'icon': 'fas fa-bolt',
        'color': '#f59e0b',
        'description': "Après chaque intervention de coupure, le rétablissement du courant est une mission critique qui exige rigueur et méthode. Nos électriciens procèdent à la vérification complète du circuit avant la remise sous tension pour assurer la sécurité totale.",
        'challenge': "Garantir un rétablissement sûr et complet du service sans risque de récidive, en vérifiant chaque point du circuit réparé.",
    },
    {
        'key': 'branchements',
        'label': 'Branchements',
        'icon': 'fas fa-plug',
        'color': '#3b82f6',
        'description': "Le raccordement de nouveaux abonnés au réseau Sonelgaz est l'une des missions les plus fréquentes. Nos équipes réalisent les travaux de tranchée, de tirage de câble et de raccordement au coffret de comptage dans le strict respect des normes Sonelgaz.",
        'challenge': "Respecter les délais stricts imposés par le client tout en appliquant les normes techniques de Sonelgaz pour un branchement durable et sécurisé.",
    },
    {
        'key': 'detecteur_co',
        'label': 'Installation des Détecteurs de Monoxyde de Carbone',
        'icon': 'fas fa-wind',
        'color': '#8b5cf6',
        'description': "Dans le cadre du programme national de sécurité domestique, Garoui Electricity déploie des détecteurs de monoxyde de carbone dans les foyers. Cette mission de prévention contribue directement à la protection des vies humaines contre ce danger invisible.",
        'challenge': "Sensibiliser les habitants et installer les détecteurs aux emplacements stratégiques (proximité des chaudières, cuisines) pour une détection optimale.",
    },
    {
        'key': 'changement_compteur',
        'label': 'Changement de Compteur',
        'icon': 'fas fa-tachometer-alt',
        'color': '#10b981',
        'description': "La modernisation du parc de compteurs est un chantier continu. Nos techniciens remplacent les anciens compteurs mécaniques par les nouveaux compteurs intelligents (prépayés ou à lecture à distance), améliorant ainsi la gestion de la consommation pour les abonnés.",
        'challenge': "Procéder au changement sans interruption prolongée du service et configurer correctement le nouveau compteur selon le contrat de l'abonné.",
    },
]

def project_list(request):
    # Fetch Sonelgaz images grouped by category key
    all_mission_images = SonelgazMissionImage.objects.all()
    images_by_category = {}
    for img in all_mission_images:
        if img.category not in images_by_category:
            images_by_category[img.category] = []
        images_by_category[img.category].append(img)

    # Merge images into categories
    missions = []
    for cat in MISSION_CATEGORIES:
        cat_copy = dict(cat)
        cat_copy['images'] = images_by_category.get(cat['key'], [])
        missions.append(cat_copy)

    return render(request, 'projects/project_list.html', {
        'missions': missions,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    other_projects = Project.objects.exclude(pk=project.pk).order_by('-year')[:3]
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'other_projects': other_projects,
    })
