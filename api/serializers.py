from rest_framework import serializers
from api.models import Company, Employee

# Create serializers here


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        # i waant to include all the field of company model
        fields = "__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # Exposing primary id
    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        # i waant to include all the field of company model
        fields = "__all__"
