from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from patient.forms import PacienteForm
from patient.models import Paciente

# PDF
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from datetime import date
from dateutil import parser


@login_required
class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente.html'


def paciente_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    paciente = get_object_or_404(Paciente, pk=pk)

    paciente.Idade = gera_idade_paciente(paciente.Data_Nascimento)

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

# Idade atual do paciente
def gera_idade_paciente(data_nascimento):
    data_atual = date.today()
    ano_atual = data_atual.year
    mes_atual = data_atual.month
    dia_atual = data_atual.day

    data_convertida = parser.parse(str(data_nascimento))
    data_nascimento = '{ano}-{mes}-{dia}'.format(ano = data_convertida.year, mes = data_convertida.month, dia = data_convertida.day)

    ano_nascimento, mes_nascimento, dia_nascimento = map(str, data_nascimento.split('-'))

    idade = ano_atual - int(ano_nascimento)

    if (mes_atual, dia_atual) < (int(mes_nascimento), int(dia_nascimento)):
        idade -= 1

    return idade

#Listagem
@login_required
def paciente(request):
    pacientes = Paciente.objects.all()

    context = {
        'pacientes': pacientes
    }
    
    pacientes = pagination(request, pacientes, 3)

    if (request.GET.get('search', '')):
        return busca_paciente(request)
    
    return render(request, 'paciente.html', {'pacientes': pacientes})


#Campo de Busca
@login_required
def busca_paciente(request):
    search_query = request.GET.get('search', '')
    if search_query:
        pacientes = Paciente.objects.filter(Nome__icontains=search_query)
    else:
        pacientes = Paciente.objects.all()
    context = {
        'pacientes': pacientes,
        'search_query': search_query,
    }

    pacientes = pagination(request, pacientes, 1)

    return render(request, 'paciente.html', {'pacientes': pacientes})

def pagination(request, pacientes, per_page = 3):
    paginator = Paginator(pacientes, per_page)
    page_number = request.GET.get('page')
    pacientes = paginator.get_page(page_number)
    
    return pacientes

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
