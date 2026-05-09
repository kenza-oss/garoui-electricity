from django.db import models

class DemandeIntervention(models.Model):
    TYPE_CHOICES = [
        ('panne_totale', 'Panne électrique totale'),
        ('panne_partielle', 'Panne partielle / Disfonctionnement'),
        ('maintenance', 'Maintenance préventive'),
        ('diagnostic', 'Diagnostic / Audit technique'),
        ('autre', 'Autre'),
    ]

    URGENCY_CHOICES = [
        ('basse', 'Basse (Planifiable)'),
        ('moyenne', 'Moyenne (Sous 48h-72h)'),
        ('haute', 'Haute (Sous 24h)'),
        ('critique', 'Critique (Arrêt de production - Immédiat)'),
    ]

    STATUS_CHOICES = [
        ('en_attente', 'En attente'),
        ('planifiee', 'Planifiée'),
        ('en_cours', 'En cours d\'intervention'),
        ('resolue', 'Résolue'),
        ('annulee', 'Annulée'),
    ]

    # Informations Client
    client_name = models.CharField(max_length=255, verbose_name="Nom complet / Contact")
    company = models.CharField(max_length=255, verbose_name="Entreprise / Établissement")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    email = models.EmailField(verbose_name="Email de contact")

    # Détails de l'intervention
    intervention_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Type d'intervention")
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES, verbose_name="Niveau d'urgence")
    
    equipment_details = models.CharField(max_length=255, blank=True, null=True, verbose_name="Équipement concerné (Optionnel)")
    description = models.TextField(verbose_name="Description détaillée du problème")
    
    address = models.TextField(verbose_name="Adresse d'intervention")
    
    # Suivi Interne
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_attente', verbose_name="Statut")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de demande")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    class Meta:
        verbose_name = "Demande d'intervention"
        verbose_name_plural = "Demandes d'intervention"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.company} - {self.get_intervention_type_display()} ({self.get_urgency_display()})"
