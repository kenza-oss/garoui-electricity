from django import forms
from .models import DemandeDevis

class DemandeDevisForm(forms.ModelForm):
    class Meta:
        model = DemandeDevis
        fields = [
            'nom_entreprise', 'nom_contact', 'poste_contact',
            'email', 'telephone', 'wilaya',
            'secteur', 'type_travaux', 'description_projet',
            'superficie', 'budget_estimatif', 'delai_souhaite',
            'plan_architectural', 'cahier_des_charges',
        ]
        widgets = {
            'nom_entreprise': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: SARL Constructions Modernes'}),
            'nom_contact': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Prénom et Nom'}),
            'poste_contact': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Directeur Technique, Maître d\'ouvrage'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'contact@entreprise.dz'}),
            'telephone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+213 5XX XX XX XX'}),
            'wilaya': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Alger, Oran, Constantine...'}),
            'secteur': forms.Select(attrs={'class': 'form-select'}),
            'type_travaux': forms.Select(attrs={'class': 'form-select'}),
            'description_projet': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 6,
                'placeholder': 'Décrivez votre projet en détail : nature des travaux, contraintes particulières, nombre de logements/bureaux, niveau de prestation souhaité...'
            }),
            'superficie': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: 5 000 m²'}),
            'budget_estimatif': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: 10 000 000 DA (facultatif)'}),
            'delai_souhaite': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: 6 mois, Livraison avant Mars 2027'}),
            'plan_architectural': forms.FileInput(attrs={'class': 'form-file', 'accept': '.pdf,.dwg,.dxf,.zip'}),
            'cahier_des_charges': forms.FileInput(attrs={'class': 'form-file', 'accept': '.pdf,.doc,.docx'}),
        }
