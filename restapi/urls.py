from rest_framework import permissions, routers

from .views import (FinancialOrganizationViewSets,
                    ExecutiveOnOrganizationViewSet,
                    ExecutiveViewSet,
                    PositionViewSet)

router = routers.DefaultRouter()

router.register('api/financial-organization', FinancialOrganizationViewSets, basename='financial-organization')
router.register('api/executive', ExecutiveViewSet, basename='executive')
router.register('api/executive-on-organization', ExecutiveOnOrganizationViewSet, basename='executive-on-organization')
router.register('api/position', PositionViewSet, basename='position')

urlpatterns = router.urls