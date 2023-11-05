from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from restapi.views import (FinancialOrganizationViewSets,
                           ExecutiveOnOrganizationViewSet,
                           ExecutiveViewSet,
                           PositionViewSet,)


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="APi for Bank Accounting Informations",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="damin_99.99@mail.ru"),
        license=openapi.License(name="Kazakhstan Government"),
    ),
    public=True,
    permission_classes=[
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    ],
)

router = routers.DefaultRouter()


router = routers.DefaultRouter()
router.register(r'financial-organization', FinancialOrganizationViewSets)
router.register(r'executive-on-organization', ExecutiveOnOrganizationViewSet)
router.register(r'executive', ExecutiveViewSet)
router.register(r'position', PositionViewSet)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('redoc/', include('django.contrib.admindocs.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)