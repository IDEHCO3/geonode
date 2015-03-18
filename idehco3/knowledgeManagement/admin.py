# -*- coding: utf-8 -*-
from django.contrib import admin

from idehco3.knowledgeManagement.models import Knowledge, Frequencia


class KnowledgeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Camada ou Mapa', {'fields' : ['camada', 'mapa']}),
        (None, {'fields' : ['usuario', 'whatFor', 'frequencia','desirable_scale','status','missing_information','resolution']}),
        ('Publicação', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
    ]

class FrequenciaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['frequencia']}),
    ]

admin.site.register(Knowledge, KnowledgeAdmin)
admin.site.register(Frequencia, FrequenciaAdmin)