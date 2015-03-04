from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from ideco.community.models import Community


#rest framework
from rest_framework.views import APIView
from rest_framework import generics

#REST api
from ideco.community.serializers import CommunitySerializer

#List communities
class CommunityList(generic.ListView):
    model = Community

class CommunityDetail(generic.DetailView):
    model = Community

class CommunityCreate(CreateView):
    model = Community
    def get_success_url(self):
        return reverse('community:detail', kwargs={'pk': self.object.pk})

class CommunityUpdate(UpdateView):
    model = Community
    fields = ['name', 'description']
    template_name_suffix = '_update_form'
    success_url = '/communities'


class CommunityDelete(DeleteView):
    model = Community
    success_url = '/communities'


class CommunityListRest(generics.ListCreateAPIView):
    """
    List all Communities, or create a new community.
    """
    queryset = Community.objects.all()

    serializer_class = CommunitySerializer

#class CommunityDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Community.objects.all()
    #serializer_class = CommunitySerializer