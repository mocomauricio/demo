from django.conf.urls import url

from django.views.generic import TemplateView


urlpatterns = [

    # La template del Dashboard 
    url('/', TemplateView.as_view(template_name="index.html"), name="index"),

]
