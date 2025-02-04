from rest_framework import serializers
from EmpApp.models import EmployeeDB

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDB
        fields = [
            'Emp_ID',
            'Name',
            'Age',
            'Company',
            'Salary',
            'Location'
        ]