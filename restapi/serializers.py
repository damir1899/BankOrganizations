from rest_framework import serializers
from main.models import (FinancialOrganization,
                     Executive,
                     ExecutiveOnOrganization,
                     Position)


class FinancialOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialOrganization
        fields = "__all__"
        

class ExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = "__all__"
        
        
class ExecutiveOnOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutiveOnOrganization
        fields = "__all__"
        
        
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"