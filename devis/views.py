from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DemandeDevisForm

def demande_devis(request):
    if request.method == 'POST':
        form = DemandeDevisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre demande de devis a été soumise avec succès ! Notre équipe vous contactera sous 48h.')
            return redirect('devis:confirmation')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    else:
        form = DemandeDevisForm()

    return render(request, 'devis/demande.html', {'form': form})


def confirmation_devis(request):
    return render(request, 'devis/confirmation.html')
