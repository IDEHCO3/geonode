from idehco3.dashboard import models

from django.views import generic

class DashboardView(generic.ListView):

    model = models.Dashboard
