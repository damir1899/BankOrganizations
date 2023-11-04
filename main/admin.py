from django.contrib import admin
from .models import (FinancialOrganization,
                     Executive,
                     ExecutiveOnOrganization,
                     Position)


admin.site.register(FinancialOrganization)
admin.site.register(Executive)
admin.site.register(ExecutiveOnOrganization)
admin.site.register(Position)
