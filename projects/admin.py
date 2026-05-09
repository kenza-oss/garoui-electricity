from django.contrib import admin
from .models import Project, ProjectCategory, ProjectGallery

class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 3

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'handle', 'icon')
    prepopulated_fields = {'handle': ('name',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'category', 'location', 'year', 'statut', 'featured')
    list_filter = ('category', 'year', 'statut', 'featured', 'wilaya')
    search_fields = ('title', 'client', 'location', 'description')
    list_editable = ('featured', 'statut')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectGalleryInline]
    fieldsets = (
        ('Informations Générales', {
            'fields': ('title', 'slug', 'client', 'category', 'description', 'main_image', 'featured', 'statut')
        }),
        ('Localisation & Calendrier', {
            'fields': ('location', 'wilaya', 'year', 'duree')
        }),
        ('Chiffres Clés', {
            'fields': ('superficie', 'puissance_installee', 'metres_cables', 'nombre_points'),
            'classes': ('collapse',)
        }),
        ('Étude de Cas', {
            'fields': ('challenge', 'solution', 'resultat'),
        }),
        ('Témoignage Client', {
            'fields': ('temoignage_client', 'temoignage_auteur'),
            'classes': ('collapse',)
        }),
        ('Produits Utilisés', {
            'fields': ('products_used',),
            'classes': ('collapse',)
        }),
    )
