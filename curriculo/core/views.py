from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import FormView
from .forms import NewCandidatoForm
from .models import Candidato
from xhtml2pdf import pisa
from .forms import NewCandidatoForm

class IndexView(TemplateView):
    template_name = 'home.html'

class CandidatoFormView(FormView):
    template_name = 'inserir_dados.html'
    form_class = NewCandidatoForm
    def form_valid(self, form):
        form.save()    
        return HttpResponseRedirect('exp/pdf')

class ErrorView(TemplateView):
    template_name = 'error.html'
    
    
#===== HTMLtoPDF =======
def render_pdf_view(request):
    candidato = Candidato.objects.last()
    
    try:
        candidato.delete()
    except:
        return HttpResponseRedirect('pdf/error')
    
    template_path = 'exportar_dados.html'
    context = {'candidato': candidato}
    
    # Create a Django response object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="MeuCurriculo.pdf"'
    
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
