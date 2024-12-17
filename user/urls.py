from django.urls import path
from .views import UserCreateAPIView, LoginView,StudentAPIView,FeesHistoryListCreateView,FeesHistoryRetrieveUpdateDeleteView
from officestaff.views import LibraryHistoryAPIView, FeesHistoryAPIView

urlpatterns = [
    path('create-user/', UserCreateAPIView.as_view(), name='api_create_user'),
    path('user/<int:pk>/', UserCreateAPIView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('students/', StudentAPIView.as_view(), name='students-list-create'),  
    path('students/<int:pk>/', StudentAPIView.as_view(), name='students-detail'),
    path('library-history/', LibraryHistoryAPIView.as_view(), name='library-history-list-create'),
    path('library-history/<int:pk>/', LibraryHistoryAPIView.as_view(), name='library-history-detail'),
    path('fees-history/', FeesHistoryListCreateView.as_view(), name='fees-history-list-create'),
    path('fees-history/<int:pk>/', FeesHistoryRetrieveUpdateDeleteView.as_view(), name='fees-history-detail'),
]