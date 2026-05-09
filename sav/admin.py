from django.contrib import admin
from .models import DemandeIntervention

@admin.register(DemandeIntervention)
class DemandeInterventionAdmin(admin.ModelAdmin):
    list_display = ('company', 'client_name', 'intervention_type', 'urgency', 'status', 'created_at')
    list_filter = ('status', 'urgency', 'intervention_type', 'created_at')
    search_fields = ('company', 'client_name', 'email', 'phone', 'address')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Informations Client', {
            'fields': ('client_name', 'company', 'phone', 'email')
        }),
        ('Détails de l\'Intervention', {
            'fields': ('intervention_type', 'urgency', 'equipment_details', 'description', 'address')
        }),
        ('Suivi Interne', {
            'fields': ('status', 'created_at', 'updated_at')
        }),
    )
