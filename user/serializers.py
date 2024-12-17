from rest_framework import serializers
from user.models import User,Student
from officestaff.models import LibraryHistory,FeesHistory

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'phone_number', 'password', 'is_office_staff', 'is_librarian','role']

    def create(self, validated_data):
        # Create the user with a hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            full_name=validated_data.get('full_name'),
            phone_number=validated_data.get('phone_number'),
            password=validated_data['password'],
            is_office_staff=validated_data.get('is_office_staff', False),
            is_librarian=validated_data.get('is_librarian', False),
        )
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','age','class_name','roll_number', 'guardian_name', 'guardian_contact',  'address', 'date_of_admission', 'section','status']

class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = ['student', 'book_name', 'borrow_date', 'return_date','status']


class FeesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesHistory
        fields = ['id', 'user', 'amount', 'payment_date', 'transaction_id', 'remarks', 'created_at', 'updated_at', 'is_paid']