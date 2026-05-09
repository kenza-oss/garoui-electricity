from django.shortcuts import render, redirect
from .models import Partner
from django.contrib import messages

def partner_list(request):
    partners = Partner.objects.filter(is_verified=True)
    return render(request, 'partners/partner_list.html', {'partners': partners})

def partner_register(request):
    if request.method == 'POST':
        # Simple processing for demonstration
        company_name = request.POST.get('company_name')
        description = request.POST.get('description')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        Partner.objects.create(
            company_name=company_name,
            description=description,
            email=email,
            phone=phone,
            address=address
        )
        messages.success(request, "Votre demande d'inscription a été soumise avec succès.")
        return redirect('partners:partner_list')
        
    return render(request, 'partners/partner_register.html')
