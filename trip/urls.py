from django.urls import path
from .views import DestinationsListView, DestinationsDetailView

urlpatterns = [
    path('', DestinationsListView.as_view(), name = 'destination_list' ),
]