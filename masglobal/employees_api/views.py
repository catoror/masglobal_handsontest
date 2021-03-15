from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView

from employees_api.DataAccess.EmployeeJsonRepository import EmployeeJsonRepository
from employees_api.Serializers.EmployeeJsonSerializer import EmployeeJsonSerializer


EXTERNAL_URL_API = "http://masglobaltestapi.azurewebsites.net/api/employees"


# Create your views here.

class EmployeeAPIView (APIView):
    """
    API endpoint that gets a list of employees with their data.
    """
    def get (self, request, *args, **kwargs):
        employee_data = EmployeeJsonRepository(EXTERNAL_URL_API)
        value_id_filter = None
        if 'id' in request.GET and request.GET["id"] != '':
            value_id_filter = request.GET["id"]
            employee_data = employee_data.get_employees_by_id(
                            id=value_id_filter)         
        else:
            employee_data = employee_data.get_employees()       

        employee_serializer = EmployeeJsonSerializer()
        obj_employee_serialized = [employee_serializer.serialize(employee)
                                   for employee in employee_data]
        return Response(obj_employee_serialized)
