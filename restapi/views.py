from rest_framework import permissions, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from main.models import (FinancialOrganization,
                         Executive,
                         ExecutiveOnOrganization,
                         Position,)

from .serializers import (FinancialOrganizationSerializer,
                          ExecutiveSerializer,
                          ExecutiveOnOrganizationSerializer,
                          PositionSerializer,)

class FinancialOrganizationViewSets(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = [SearchFilter, OrderingFilter]
    queryset = FinancialOrganization.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    ]
    serializer_class = FinancialOrganizationSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)  
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class ExecutiveViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = [SearchFilter, OrderingFilter]
    queryset = Executive.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    ]
    serializer_class = ExecutiveSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)  
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class ExecutiveOnOrganizationViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = [SearchFilter, OrderingFilter]
    queryset = ExecutiveOnOrganization.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    ]
    serializer_class = ExecutiveOnOrganizationSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)  
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
class PositionViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = [SearchFilter, OrderingFilter]
    queryset = Position.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    ]
    serializer_class = PositionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)  
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
