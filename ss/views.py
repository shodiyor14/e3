from django.shortcuts import render
from ss.models import Watches
from django.views.generic import TemplateView

class WatchesViews(TemplateView):
    template_name = 'gallery.html'

