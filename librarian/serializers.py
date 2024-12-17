from rest_framework import serializers
from officestaff.models import LibraryHistory

from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
       
        return value

    def validate_password(self, value):
        
        return value
