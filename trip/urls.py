from django.urls import path
from .views import DestinationsListView,  DestinationsDetailView, DestinationsUpdateView, DestinationsCreateView, DestinationsDeleteView

urlpatterns = [
    path('', DestinationsListView.as_view(), name = 'destination_list' ),
    path('destination/<int:pk>/', DestinationsDetailView.as_view(), name = 'destination_detail' ),
    path('destination/<int:pk>/edit', DestinationsUpdateView.as_view(), name="destination_update"),
    path('destination/new/', DestinationsCreateView.as_view(), name = 'destination_create' ),
    path('destination/<int:pk>/delete', DestinationsDeleteView.as_view(), name="destination_delete"),
]

    