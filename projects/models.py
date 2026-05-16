from django.db import models
from django.utils.text import slugify

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    handle = models.SlugField(unique=True)
    icon = models.CharField(max_length=100, default='fas fa-bolt', verbose_name="Icône FontAwesome")

    class Meta:
        verbose_name = "Catégorie de Projet"
        verbose_name_plural = "Catégories de Projets"

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUT_CHOICES = [
        ('en_cours', 'En Cours'),
        ('termine', 'Terminé'),
        ('livré', 'Livré'),
    ]

    title = models.CharField(max_length=255, verbose_name="Titre du projet")
    slug = models.SlugField(unique=False, blank=True)
    client = models.CharField(max_length=255, blank=True, verbose_name="Client / Maître d'ouvrage")
    description = models.TextField(verbose_name="Description courte")
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, verbose_name="Catégorie")
    location = models.CharField(max_length=255, verbose_name="Localisation")
    wilaya = models.CharField(max_length=100, blank=True, verbose_name="Wilaya")
    year = models.IntegerField(verbose_name="Année de réalisation")
    duree = models.CharField(max_length=100, blank=True, verbose_name="Durée du chantier")
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='termine', verbose_name="Statut")
    main_image = models.ImageField(upload_to='projects/', verbose_name="Image principale")
    featured = models.BooleanField(default=False, verbose_name="Projet mis en avant")

    # Chiffres clés
    superficie = models.CharField(max_length=100, blank=True, verbose_name="Superficie (m²)")
    puissance_installee = models.CharField(max_length=100, blank=True, verbose_name="Puissance installée (kVA/kW)")
    metres_cables = models.CharField(max_length=100, blank=True, verbose_name="Mètres de câbles")
    nombre_points = models.CharField(max_length=100, blank=True, verbose_name="Nombre de points d'éclairage")

    # Étude de cas (case study)
    challenge = models.TextField(blank=True, verbose_name="Le Défi")
    solution = models.TextField(blank=True, verbose_name="Notre Solution")
    resultat = models.TextField(blank=True, verbose_name="Les Résultats")
    temoignage_client = models.TextField(blank=True, verbose_name="Témoignage client")
    temoignage_auteur = models.CharField(max_length=200, blank=True, verbose_name="Auteur du témoignage")

    # Association with products
    products_used = models.ManyToManyField('shop.Product', blank=True, verbose_name="Produits utilisés")

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Projet / Réalisation"
        verbose_name_plural = "Projets / Réalisations"
        ordering = ['-year', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.year})"


class ProjectGallery(models.Model):
    project = models.ForeignKey(Project, related_name='gallery', on_delete=models.CASCADE, verbose_name="Projet")
    image = models.ImageField(upload_to='projects/gallery/', verbose_name="Image")
    legende = models.CharField(max_length=255, blank=True, verbose_name="Légende")

    class Meta:
        verbose_name = "Photo de galerie"
        verbose_name_plural = "Photos de galerie"


class SonelgazMissionImage(models.Model):
    CATEGORY_CHOICES = [
        ('coupure', 'Coupure'),
        ('retablissement', 'Rétablissement'),
        ('branchements', 'Branchements'),
        ('detecteur_co', 'Détecteur de Monoxyde de Carbone'),
        ('changement_compteur', 'Changement de Compteur'),
    ]
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        verbose_name="Catégorie de mission"
    )
    image = models.ImageField(upload_to='sonelgaz/', verbose_name="Photo")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Légende (optionnel)")

    class Meta:
        verbose_name = "Image de mission Sonelgaz"
        verbose_name_plural = "Images de missions Sonelgaz"
        ordering = ['category']

    def __str__(self):
        return f"{self.get_category_display()} - {self.caption or 'Image'}"

