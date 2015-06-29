from django.shortcuts import render
from django.views import generic
from .models import Band

default_pagination = 3

class IndexView(generic.ListView):
    template_name = 'bands/index.html'
    context_object_name = 'all_bands'
    model = Band
    paginate_by = default_pagination

    def get_context_object(self):
        return Band.objects.all().order_by('name')

class BandView(generic.DetailView):
    template_name = 'bands/band.html'
    context_object_name = 'band'
    model = Band
