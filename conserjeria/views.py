from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import models


def index(request):
    residencias_list = models.Residencia.objects.all()
    correspondencia_list = models.Correspondencia.objects.filter(entregado=False).order_by('-fecha')

    template = loader.get_template('correspondencia/index.html')
    context = {
        "residencias_list": residencias_list,
        "correspondencia_list": correspondencia_list,
    }
    return HttpResponse(template.render(context, request))

def residencia(request, residencia_id):
    correspondencia_list = models.Correspondencia.objects.filter(entregado=False, residencia=residencia_id).order_by('-fecha')
    residencia_actual = models.Residencia.objects.get(pk=residencia_id)

    template = loader.get_template('correspondencia/residencia.html')
    context = {
        "correspondencia_list": correspondencia_list,
        "residencia_actual": residencia_actual,
    }
    return HttpResponse(template.render(context, request))
