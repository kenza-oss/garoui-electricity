from django import forms
from .models import DemandeIntervention

class DemandeInterventionForm(forms.ModelForm):
    class Meta:
        model = DemandeIntervention
        fields = [
            'client_name', 'company', 'phone', 'email',
            'intervention_type', 'urgency', 'equipment_details',
            'description', 'address'
        ]
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Votre nom et prénom'}),
            'company': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nom de votre entreprise'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'N° de téléphone (joignable)'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Adresse email professionnelle'}),
            
            'intervention_type': forms.Select(attrs={'class': 'form-input'}),
            'urgency': forms.Select(attrs={'class': 'form-input'}),
            
            'equipment_details': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: TGBT, Transformateur, Groupe Électrogène...'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Décrivez précisément le problème ou la panne rencontrée...'}),
            
            'address': forms.Textarea(attrs={'class': 'form-input', 'rows': 2, 'placeholder': 'Adresse complète du site d\'intervention'}),
        }
