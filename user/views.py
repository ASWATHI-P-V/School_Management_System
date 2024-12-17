from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializers import UserSerializer,StudentSerializer, FeesHistorySerializer
from officestaff.serializers import LibraryHistorySerializer
from user.models import User,Student
from officestaff.models import LibraryHistory,FeesHistory
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from user.permission import IsAdminUserOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class LoginView(APIView):
    def post(self, request):
        
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            
            user = User.objects.filter(email=email).first()

            if user and user.check_password(password): 
                
                if user.role == 'admin':
                    
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'access_token': str(refresh.access_token),
                        'refresh_token': str(refresh),
                    }, status=200)
                else:
                    return Response({'detail': 'User is not an admin.'}, status=403)
            else:
                return Response({'detail': 'Invalid credentials or unauthorized user.'}, status=401)

        return Response(serializer.errors, status=400)

class LogoutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

class UserCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAdminUserOrReadOnly] 
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk, *args, **kwargs):
        """
        Retrieve details of a specific user.
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        """
        Update a user.
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        """
        Delete a user.
        """
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class StudentAPIView(APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAdminUserOrReadOnly]
    # Create a new student
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student created successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve, update, or delete a specific student
    def get_object(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk=None):
        if pk:
            student = self.get_object(pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class LibraryHistoryAPIView(APIView):
    authentication_classes = [JWTAuthentication]  # Use JWT for authentication
    permission_classes = [IsAdminUserOrReadOnly]
    # Create a new library history record
    def post(self, request, *args, **kwargs):
        serializer = LibraryHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Library history created successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve, update, or delete a specific library history record
    def get_object(self, pk):
        return get_object_or_404(LibraryHistory, pk=pk)

    def get(self, request, pk=None):
        if pk:
            library_history = self.get_object(pk)
            serializer = LibraryHistorySerializer(library_history)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            library_histories = LibraryHistory.objects.all()
            serializer = LibraryHistorySerializer(library_histories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        library_history = self.get_object(pk)
        serializer = LibraryHistorySerializer(library_history, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Library history updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        library_history = self.get_object(pk)
        library_history.delete()
        return Response({"message": "Library history deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class FeesHistoryListCreateView(APIView):
    authentication_classes = [JWTAuthentication]  # Use JWT for authentication
    permission_classes = [IsAdminUserOrReadOnly]
    """
    List all FeesHistory records or create a new one.
    """
    def get(self, request, format=None):
        fees_history = FeesHistory.objects.all()
        serializer = FeesHistorySerializer(fees_history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = FeesHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeesHistoryRetrieveUpdateDeleteView(APIView):
    """
    Retrieve, update, or delete a specific FeesHistory record.
    """
    def get_object(self, pk):
        return get_object_or_404(FeesHistory, pk=pk)

    def get(self, request, pk, format=None):
        fees_history = self.get_object(pk)
        serializer = FeesHistorySerializer(fees_history)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        fees_history = self.get_object(pk)
        serializer = FeesHistorySerializer(fees_history, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fees_history = self.get_object(pk)
        fees_history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)