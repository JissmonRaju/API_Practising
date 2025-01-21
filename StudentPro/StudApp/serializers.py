from rest_framework import serializers
from StudApp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = {
            'StudId',
            'Name',
            'Place',
            'Course',
            'Address',
            'Age'
        }