from django.views.generic import ListView, DetailView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Destinations

class DestinationsListView(ListView):
    template_name = "destination_list.html"
    model = Destinations

class DestinationsDetailView(DetailView):
    template_name = "destination_detail.html"
    model = Destinations

# class DestinationsUpdatelView(UpdateView):
#     template_name = "destiation_Update.html"
#     model = Destinations


