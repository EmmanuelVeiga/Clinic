from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from patient.forms import PacienteForm
from patient.models import Paciente

# PDF
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


@login_required
class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente.html'


def paciente_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    paciente = get_object_or_404(Paciente, pk=pk)

    template_path = 'pdf1.html'
    context = {'paciente': paciente}

    # Crie um objeto de resposta do Django e especifique content_type como pdf
    response = HttpResponse(content_type='application/pdf')

    # Para Download Use esse Trecho
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # encontre o modelo e renderize-o.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # se houver erro, mostre uma visão engraçada
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Criação PDF
def render_pdf_view(request):
    template_path = 'pdf1.html'
    context = {'myvar': 'TESTE CRIAÇÃO PDF'}

    # Crie um objeto de resposta do Django e especifique content_type como pdf
    response = HttpResponse(content_type='application/pdf')

    # Para Download Use esse Trecho
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # encontre o modelo e renderize-o.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # se houver erro, mostre uma visão engraçada
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def home(request):
    return render(request, 'home.html')

@login_required
def paciente(request):
    pacientes = Paciente.objects.all()
    context = {
        'pacientes': pacientes
    }
    return render(request, 'paciente.html', context)

@login_required
def paciente_add(request):
    form = PacienteForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('paciente')
    context = {
        'form': form
    }
    return render(request, 'paciente_add.html', context)

@login_required
def paciente_edit(request, paciente_pk):
    paciente = Paciente.objects.get(pk=paciente_pk)
    form = PacienteForm(request.POST or None, instance=paciente)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('paciente')

    context = {
        'form': form,
        'paciente': paciente.id,
    }
    return render(request, 'paciente_edit.html', context)

@login_required
def paciente_delete(request, paciente_pk):
    paciente = Paciente.objects.get(pk=paciente_pk)
    paciente.delete()
    return redirect('paciente')
