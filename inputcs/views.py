from django.shortcuts import render, HttpResponse
# from django.db.models import Count
from django.views.generic.base import TemplateView
from django.utils import timezone
from django.urls import reverse_lazy, reverse  
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView, CreateView
from . import models, forms
from inputcs.models import Post, AjaxImage
from inputcs.forms import PostForm, AjaxImageForm
import json

from django.http import HttpResponse, JsonResponse, Http404
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.db.models import F

class HomeView(TemplateView):
    """
    The CS homepage
    """
    template_name = 'inputcs/home.html'

    def get_context_data(self, **kwargs):
        sheet_form = forms.SheetForm
        context = super().get_context_data(**kwargs)
        
        context['sheet_form'] = sheet_form
        
        return context
    
class InputView(TemplateView):
    """
    Defect input
    """
    template_name = 'inputcs/input.html'

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
        'coorx',
        'coory',
    ]
    def form_valid(self, form):
        messages.add_message(
        self.request,
        messages.SUCCESS,
        'Thank you! Your photo has been saved.'
    )
        return super().form_valid(form)

class HomeView2(TemplateView):
    """
    The CS homepage2
    """
    template_name = 'inputcs/home2.html'

def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        post_coord = request.POST.get('the_coord')
        response_data = {}

        post = Post(text=post_text, author=request.user, coord=post_coord)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['coord'] = post.coord
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def ajaximage(request):
    coord = AjaxImage.objects.order_by('-id')[:5]
    # context = { 'coord' : coord }
    form = AjaxImageForm()
    if request.method == "POST" and request.is_ajax():
        form = AjaxImageForm(request.POST)
        if form.is_valid():
            image_coord = form.cleaned_data['image_coord']
            form.save()
            return JsonResponse({"image_coord": image_coord}, status=200)

    return render(request, "inputcs/imageajax.html", {'form':form})
    

# class AjaxFormView(CreateView):
#     model = models.Ajaxd
#     success_url = reverse_lazy('ajax')
#     fields = [
#         'test',
#     ]
    
#     def form_valid(self, form):
#         messages.add_message(
#             self.request,
#             messages.SUCCESS,
#             'Thank you! Your message has been sent.'
#         )
#         return super().form_valid(form)