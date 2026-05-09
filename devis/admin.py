from django.contrib import admin
from .models import DemandeDevis

@admin.register(DemandeDevis)
class DemandeDevisAdmin(admin.ModelAdmin):
    list_display = ('nom_entreprise', 'nom_contact', 'email', 'telephone', 'secteur', 'type_travaux', 'statut', 'date_soumission')
    list_filter = ('statut', 'secteur', 'type_travaux')
    search_fields = ('nom_entreprise', 'nom_contact', 'email', 'wilaya')
    readonly_fields = ('date_soumission', 'date_modification')
    list_editable = ('statut',)
    ordering = ('-date_soumission',)
    fieldsets = (
        ('Informations Contact', {
            'fields': ('nom_entreprise', 'nom_contact', 'poste_contact', 'email', 'telephone', 'wilaya')
        }),
        ('Détails du Projet', {
            'fields': ('secteur', 'type_travaux', 'description_projet', 'superficie', 'budget_estimatif', 'delai_souhaite')
        }),
        ('Documents Joints', {
            'fields': ('plan_architectural', 'cahier_des_charges')
        }),
        ('Gestion Interne', {
            'fields': ('statut', 'notes_internes', 'date_soumission', 'date_modification')
        }),
    )
