from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import User
from .permissions import IsLibrarian
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import AllowAny
from rest_framework import status
from user.serializers import StudentSerializer
from officestaff.serializers import LibraryHistorySerializer
from user.models import Student
from officestaff.models import LibraryHistory
from rest_framework.generics import RetrieveAPIView, ListAPIView
from librarian.permissions import IsLibrarian

class LibrarianLoginView(APIView):
    

    def post(self, request):
        # Get email and password from the request
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Fetch the user using the email
            user = User.objects.filter(email=email).first()

            if user and user.check_password(password):  # Check if passwords match
                # Check if the user is a librarian
                if user.role == 'librarian':
                    # Generate JWT token for the librarian user
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'access_token': str(refresh.access_token),
                        'refresh_token': str(refresh),
                    }, status=200)
                else:
                    return Response({'detail': 'User is not a librarian.'}, status=403)
            else:
                return Response({'detail': 'Invalid credentials or unauthorized user.'}, status=401)

        return Response(serializer.errors, status=400)

class LibraryHistoryListAPIView(APIView):
    permission_classes = [IsLibrarian]  

    def get(self, request):
        # Fetch all library history records
        library_histories = LibraryHistory.objects.all()
        serializer = LibraryHistorySerializer(library_histories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# List all students
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsLibrarian]    # Adjust permissions as needed

# Retrieve a specific student by primary key
class StudentDetailAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsLibrarian]    # Adjust permissions as needed
