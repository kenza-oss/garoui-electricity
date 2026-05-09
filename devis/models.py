from django.db import models

class DemandeDevis(models.Model):
    SECTEUR_CHOICES = [
        ('residentiel', 'Résidentiel (AADL, Villas, Cités)'),
        ('hospitalier', 'Hospitalier (Hôpitaux, Cliniques)'),
        ('touristique', 'Touristique & Tertiaire (Hôtels, Centres commerciaux)'),
        ('industriel', 'Industriel (Usines, Entrepôts)'),
        ('autre', 'Autre'),
    ]

    TYPE_TRAVAUX_CHOICES = [
        ('courant_fort', 'Courant Fort (Puissance)'),
        ('courant_faible', 'Courant Faible (Données, Sécurité)'),
        ('domotique', 'Domotique & Smart Home'),
        ('maintenance', 'Maintenance & Diagnostic'),
        ('mixte', 'Projet Mixte (Plusieurs types)'),
    ]

    STATUT_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('en_cours', 'En cours de traitement'),
        ('devis_envoye', 'Devis envoyé'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
    ]

    # Informations sur l'entreprise/client
    nom_entreprise = models.CharField(max_length=200, verbose_name="Nom de l'entreprise / Promoteur")
    nom_contact = models.CharField(max_length=150, verbose_name="Nom du contact")
    poste_contact = models.CharField(max_length=100, blank=True, verbose_name="Poste / Fonction")
    email = models.EmailField(verbose_name="Email professionnel")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    wilaya = models.CharField(max_length=100, blank=True, verbose_name="Wilaya / Région")

    # Détails du projet
    secteur = models.CharField(max_length=50, choices=SECTEUR_CHOICES, verbose_name="Secteur d'activité")
    type_travaux = models.CharField(max_length=50, choices=TYPE_TRAVAUX_CHOICES, verbose_name="Type de travaux")
    description_projet = models.TextField(verbose_name="Description détaillée du projet")
    superficie = models.CharField(max_length=100, blank=True, verbose_name="Superficie approximative (m²)")
    budget_estimatif = models.CharField(max_length=100, blank=True, verbose_name="Budget estimatif (facultatif)")
    delai_souhaite = models.CharField(max_length=100, blank=True, verbose_name="Délai souhaité")

    # Documents
    plan_architectural = models.FileField(
        upload_to='devis/plans/',
        blank=True, null=True,
        verbose_name="Plan architectural (PDF, DWG, DXF)"
    )
    cahier_des_charges = models.FileField(
        upload_to='devis/cdc/',
        blank=True, null=True,
        verbose_name="Cahier des charges (PDF)"
    )

    # Gestion interne
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='nouveau', verbose_name="Statut")
    notes_internes = models.TextField(blank=True, verbose_name="Notes internes")
    date_soumission = models.DateTimeField(auto_now_add=True, verbose_name="Date de soumission")
    date_modification = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")

    class Meta:
        verbose_name = "Demande de Devis"
        verbose_name_plural = "Demandes de Devis"
        ordering = ['-date_soumission']

    def __str__(self):
        return f"[{self.get_statut_display()}] {self.nom_entreprise} - {self.get_secteur_display()}"
