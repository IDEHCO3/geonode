# Create your views here.
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from idehco3.tweeterStream.models import *
from idehco3.utils.utils import JsonResponse

def getTwitterMapData(request):
    search = ""
    if not request.POST.has_key("searchTweets") and not request.GET.has_key("searchTweets"):
        return JsonResponse("")

    if request.method == "POST":
        search = request.POST["searchTweets"]
    if request.method == "GET":
        search = request.GET["searchTweets"]

    data = getGeoJsonTwitter(search)
    return JsonResponse(data)


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
