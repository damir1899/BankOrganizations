from django.urls import path

from .views import (IndexView, 
                    OrganizationCardView)


urlpatterns = [
    path('', IndexView),
    path('<slug:slug>/', OrganizationCardView, name='product_detail'),

]