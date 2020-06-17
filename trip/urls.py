from django.urls import path
from .views import DestinationsListView,  DestinationsDetailView, DestinationsCreateView

urlpatterns = [
    path('', DestinationsListView.as_view(), name = 'destination_list' ),
    path('destination/<int:pk>/', DestinationsDetailView.as_view(), name = 'destination_detail' ),
    path('destination/new/', DestinationsCreateView.as_view(), name = 'destination_create' ),
]