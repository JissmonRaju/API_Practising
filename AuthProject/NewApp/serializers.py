from rest_framework import serializers
from NewApp.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id','name','email','password'
        )

    def create(self, validated_data):
        pwd = validated_data.pop('password',None)
        inst = self.Meta.model(**validated_data)
        if pwd is not None:
            inst.set_password(pwd)
        inst.save()
        return inst