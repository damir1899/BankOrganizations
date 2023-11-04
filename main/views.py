from django.shortcuts import render, get_object_or_404
from .models import (FinancialOrganization,
                     Executive,
                     ExecutiveOnOrganization)

def IndexView(request):
    data = FinancialOrganization.objects.all()
    context = {
        'data': data
    }
    return render(request, 'main/index.html', context=context)


def OrganizationCardView(request, slug):
    organization = get_object_or_404(FinancialOrganization, slug=slug)
    directors = ExecutiveOnOrganization.objects.filter(organization=organization)
    
    executives_by_position = {}
    for director in directors:
        for position in director.executive.position.all():
            if position:
                if position in executives_by_position:
                    executives_by_position[position].append(director.executive)
                else:
                    executives_by_position[position] = [director.executive]
                
    context = {
        'organization': organization,
        'executives_by_position': executives_by_position,
    }
    
    return render(request, 'main/card.html', context=context)
    
