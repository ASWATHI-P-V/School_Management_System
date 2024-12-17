from django.urls import path
from .views import OfficeStaffLoginView,FeesHistoryAPIView,LibraryHistoryAPIView, StudentListAPIView, StudentDetailAPIView

urlpatterns = [
    path('login/', OfficeStaffLoginView.as_view(), name='officestaff-login'),
    path('fees-history/', FeesHistoryAPIView.as_view(), name='fees-history'),
    path('fees-history/<int:pk>/', FeesHistoryAPIView.as_view(), name='fees-history-detail'),
    path('library/', LibraryHistoryAPIView.as_view(), name='library-list-create'),
    path('library/<int:pk>/', LibraryHistoryAPIView.as_view(), name='library-detail'),
    path('students-details/',StudentListAPIView.as_view(), name='student-list'),
    path('students-details/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
]
