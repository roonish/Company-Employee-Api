from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Model view set contain all the functins CRUD
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # for custom api  i.e.
    # /company/companyid/employees, which doesnot exist till now

    # detail true means companyid  must be passed

    # url auxa /company hunxa, then ya detail true le id halnai parxa so /company/id/ hunxa
    # then tala employee pathaunu parxa to get employees.
    # companies/{companyId}/employees
    @action(detail=True, methods=["get"])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)

            # serialize emps to convert  object into json
            emps_serializer = EmployeeSerializer(
                emps, many=True, context={"request": request}
            )
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({"message": "Company might not exist!! Error"})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
