# from django.shortcuts import render
# from django.db.models import Count
from django.views.generic.base import TemplateView
from django.utils import timezone
from django.urls import reverse_lazy, reverse  
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView, CreateView
from . import models, forms
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.db.models import F

class HomeView(TemplateView):
    """
    The Blog homepage
    """
    template_name = 'inputcs/home.html'

    def get_context_data(self, **kwargs):
        sheet_form = forms.SheetForm
        context = super().get_context_data(**kwargs)

        context['sheet_form'] = sheet_form
        
        return context

    

class DefectFormView(CreateView):
    model = models.Sheet
    success_url = reverse_lazy('home')
    fields = [
        'process',
        'defect',
        'period',
    ]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your message has been sent.'
        )
        return super().form_valid(form)