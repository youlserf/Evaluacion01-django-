from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Candidato, Region

def index(request):
    latest_question_list = Region.objects.order_by('-id')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, './encuesta_region/index.html', context)

def detalle(request, region_id):
    region =  get_object_or_404(Region, pk=region_id)
    return render(request, 'encuesta_region/detalle.html', {'region': region})
                
def votar(request, region_id):
         region = get_object_or_404(Region, pk=region_id)
         p = Candidato( nombres= request.POST['nombres'],
                    apellidos = request.POST['apellidos'],
                    partido_politico  = request.POST['partido_politico'],
                    region_id = request.POST['region_id']
         )
         p.save()
         return HttpResponseRedirect(reverse('encuesta_region:resultados', args=(region.id,)))

def actualizar(request):
    record = Candidato.objects.filter(id = request.POST['id_candidato'],)
    record.update(
        nombres= request.POST['nombres'],
        apellidos = request.POST['apellidos'],
        partido_politico  = request.POST['partido_politico'],
        region_id = request.POST['region_id']
    )
    latest_question_list = Region.objects.order_by('-id')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, './encuesta_region/index.html', context)



def eliminar(request, region_id):
    region =  get_object_or_404(Region, pk=region_id)
    record = Candidato.objects.get(id = request.POST['id_candidato'],)
    record.delete()
    return HttpResponseRedirect(reverse('encuesta_region:detalle', args=(region.id,)))


def actualizar_view(request, region_id):
    region =  get_object_or_404(Region, pk=region_id)
    candidato = Candidato.objects.get(id = request.POST['id_candidato'],)
    latest_question_list = Region.objects.order_by('-id')
    return render(request, 'encuesta_region/actualizar.html', {'candidato': candidato, 'region': latest_question_list})

def resultados(request, region_id):
    latest_question_list = Region.objects.order_by('-id')
    region = get_object_or_404(Region, pk=region_id)
    return render(request, 'encuesta_region/resultados.html', {'region': region, 'latest_question_list': latest_question_list})