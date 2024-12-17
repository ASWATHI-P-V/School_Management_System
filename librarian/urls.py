from django.urls import path
from .views import LibrarianLoginView,LibraryHistoryListAPIView, StudentListAPIView, StudentDetailAPIView

urlpatterns = [
    
    path('login/', LibrarianLoginView.as_view(), name='librarian-login'),
    path('library-details/', LibraryHistoryListAPIView.as_view(), name='library-list'),
    path('library-details/<int:pk>/', LibraryHistoryListAPIView.as_view(), name='library-detail'),
    path('students-details/',StudentListAPIView.as_view(), name='student-list'),
    path('students-details/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),

]


  
