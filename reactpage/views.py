from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

############################################################
# La clase TemplateView es una vista genérica que se 
# usa generalmente para renderizar una página estática,
# mas info: https://docs.djangoproject.com/en/3.1/topics/class-based-views/
#
# El decorador que tiene es para que requiera iniciar estar 
# logueado para visualizar la página, si no estás logueado
# te redirije automáticamente al login 
#
# Acá uso para renderizar una págica generada con react-create-app,
# al archivo compilado con "yarn build" (build/index.html) le edite para que encuentre
# los archivos estáticos (.css, .js, .json, etc) y copié todos los estáticos
# alguna carpeta static configurado en el proyecto de django
# despues copie el index.html alguna carpeta de templates,
# en este caso le renombré porque ya tengo un index.html
############################################################

@method_decorator(login_required, name='dispatch')
class ReactPageView(TemplateView):
    template_name = "reactpage.html"