from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView,DeleteView

from ideco.sdi_management.models import InstanceSDICo

#List GeoProjects
class InstanceSDICoList(generic.ListView):
    model = InstanceSDICo

class InstanceSDICoCreate(CreateView):
    model = InstanceSDICo
    def get_success_url(self):
        return reverse('sdi_management:detail', kwargs={'pk': self.object.pk})

