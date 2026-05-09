from django.core.management.base import BaseCommand
from projects.models import Project, ProjectCategory
from shop.models import Product
from django.core.files.base import ContentFile
import requests

class Command(BaseCommand):
    help = 'Seed projects'

    def handle(self, *args, **kwargs):
        cat_hosp, _ = ProjectCategory.objects.get_or_create(name='Hospitalier', handle='hospitalier')
        cat_ind, _ = ProjectCategory.objects.get_or_create(name='Industriel', handle='industriel')
        cat_res, _ = ProjectCategory.objects.get_or_create(name='Résidentiel', handle='residentiel')

        projects_data = [
            {
                'title': 'Hôpital Militaire d\'Alger',
                'description': 'Installation complète du système d\'alimentation de secours et des tableaux TGBT de haute sécurité.',
                'category': cat_hosp,
                'location': 'Alger',
                'year': 2024,
                'challenge': 'Garantir une continuité de service 24h/24 sans aucune micro-coupure.',
                'solution': 'Mise en place d\'un système redondant de groupes électrogènes couplés à des onduleurs de forte puissance.'
            },
            {
                'title': 'Promotion Immobilière AADL 2000 Logements',
                'description': 'Déploiement du réseau électrique basse tension et installation de l\'éclairage public LED pour l\'ensemble du site.',
                'category': cat_res,
                'location': 'Oran',
                'year': 2023,
                'challenge': 'Optimisation énergétique pour réduire les coûts de maintenance de la cité.',
                'solution': 'Utilisation de projecteurs LED ELMARK avec capteurs de luminosité intelligents.'
            }
        ]

        for data in projects_data:
            project, created = Project.objects.get_or_create(
                title=data['title'],
                defaults={
                    'description': data['description'],
                    'category': data['category'],
                    'location': data['location'],
                    'year': data['year'],
                    'challenge': data['challenge'],
                    'solution': data['solution']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created project "{project.title}"'))
            else:
                self.stdout.write(self.style.WARNING(f'Project "{project.title}" already exists'))
