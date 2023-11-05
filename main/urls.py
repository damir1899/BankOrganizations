from django.urls import path

from .views import (IndexView, 
                    OrganizationCardView,
                    ExecutiveCardView)


urlpatterns = [
    path('', IndexView),
    path('organization/<slug:slug>/', OrganizationCardView, name='organization_card'),
    path('executive/<slug:slug>/', ExecutiveCardView, name='executive_card'),

]