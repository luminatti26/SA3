from django.urls import path

from Mysite.views import index_pag, plantas_pag, contato_pag


urlpatterns = [
    path('', index_pag, name='index'),
    path('plantas', plantas_pag, name='plantas'),
    path('contato', contato_pag, name='contato')
]
