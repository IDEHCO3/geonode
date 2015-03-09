# Create your views here.
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from idehco3.tweeterStream.models import *


class TweeterStreamList(generic.ListView):
    model = TweeterStream

class TweeterStreamDetail(generic.DetailView):
    model = TweeterStream

class TweeterStreamCreate(CreateView):
    model = TweeterStream
    def get_success_url(self):
        return reverse('tweeterStream:detail', kwargs={'pk': self.object.pk})

class TweeterStreamUpdate(UpdateView):
    model = TweeterStream
    fields = ['name', 'description', 'init_date', 'end_date']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse('tweeterStream:list')

class TweeterStreamDelete(DeleteView):
    model = TweeterStream
    def get_success_url(self):
        return reverse('tweeterStream:list')