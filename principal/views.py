from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

############################################################
# La clase TemplateView se usa es una vista genérica que se 
# usa generalmente para renderizar una página estática,
# mas info: https://docs.djangoproject.com/en/3.1/topics/class-based-views/
#
# El decorador que tiene es para que requiera iniciar estar 
# logueado para visualizar la página, si no estás logueado
# te redirije automáticamente al login 
############################################################

@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = "index.html"

@method_decorator(login_required, name='dispatch')
class CardsView(TemplateView):
    template_name = "cards.html"

@method_decorator(login_required, name='dispatch')
class ChartsView(TemplateView):
    template_name = "charts.html"

@method_decorator(login_required, name='dispatch')
class TablesView(TemplateView):
    template_name = "tables.html"

@method_decorator(login_required, name='dispatch')
class NavbarView(TemplateView):
    template_name = "navbar.html"