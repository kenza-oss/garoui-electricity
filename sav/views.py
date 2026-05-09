from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DemandeInterventionForm

def intervention_request(request):
    if request.method == 'POST':
        form = DemandeInterventionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sav:intervention_success')
    else:
        form = DemandeInterventionForm()

    return render(request, 'sav/intervention_form.html', {'form': form})

def intervention_success(request):
    return render(request, 'sav/intervention_success.html')
