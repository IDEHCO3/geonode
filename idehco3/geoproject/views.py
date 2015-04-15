from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView,DeleteView

from idehco3.geoproject.models import Project

#List GeoProjects
class GeoProjectList(generic.ListView):
    model = Project
    template_name = 'geoproject/geoproject_index.html'

class GeoProjectCreate(CreateView):
    model = Project
    def get_success_url(self):
        return reverse('geoproject:detail', kwargs={'pk': self.object.pk})

