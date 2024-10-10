"""
URL configuration for sga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplic.urls')),
]


from rest_framework.routers import SimpleRouter
from django.urls import path
from django import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
router = SimpleRouter()

urlpatterns = [

    path('novo/', views.criar_usuario, name='criar_usuario'),
    path('<int:pk>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('novo/', views.criar_conteudo, name='criar_conteudo'),
    path('<int:pk>/aprovar/', views.reportar_post, name='reportar_post'),
    path('', views.listar_avaliacoes, name='lista_avaliacoes'),
    path('novo/', views.criar_avaliacao, name='criar_avaliacao'),





]