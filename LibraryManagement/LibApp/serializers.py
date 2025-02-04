from rest_framework import serializers
from LibApp.models import Library

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = (
            'UserId',
            'UserName',
            'Age',
            'Mobile',
            'Email_Id',
            'Place',
            'Profile_Image'
        )
