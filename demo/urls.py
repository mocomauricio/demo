"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import include

urlpatterns = [
    # incluimos las urls del sitio de Administracion de django, 
    # el dashboard por defecto de Django que debería utilizarse para 
    # administración del sitio principal
    path('admin/', admin.site.urls),

    # incluimos las urls de nuestra API rest del modelo Snippets
    path('api/', include("snippets.api_urls")),

    # incluimos las urls de nuestro CRUD del modelo Snippet
    path('snippets/', include("snippets.urls")),

    # incluimos las urls de nuestro CRUD del modelo Snippet
    path('reactpage/', include("reactpage.urls")),

    # incluimos las urls de nuestro sitio custom  
    path('', include("principal.urls")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

