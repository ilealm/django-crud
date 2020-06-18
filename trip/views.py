from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Destinations

class DestinationsListView(ListView):
    template_name = "destination_list.html"
    model = Destinations

class DestinationsDetailView(DetailView):
    template_name = "destination_detail.html"
    model = Destinations

class DestinationsUpdateView(UpdateView):
    template_name = "destination_update.html"
    model = Destinations
    fields = ['place', 'location', 'summary']

class DestinationsCreateView(CreateView):
    template_name = "destination_create.html"
    model = Destinations
    fields = ['author', 'place', 'location', 'summary']

class DestinationsDeleteView(DeleteView):
    template_name = "destination_delete.html"
    model = Destinations
    success_url = reverse_lazy('destination_list')