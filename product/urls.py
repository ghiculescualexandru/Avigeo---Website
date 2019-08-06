from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path ('despre_noi', views.DespreNoi.as_view(), name='despre_noi'),
    path ('catalog/', views.inspiratie, name='inspiratie'),
    path ('inspiratie/tiparDigital/', views.tipar_digital, name='tipar_digital'),
    path ('inspiratie/printOutdoor/', views.print_outdoor, name='print_outdoor'),
    path ('inspiratie/printIndoor/', views.print_indoor, name='print_indoor'),
    path ('inspiratie/tiparOffset/', views.tipar_offset, name='tipar_offset'),
    path ('inspiratie/litereVolumetrice/', views.litere_volumetrice, name='litere_volumetrice'),
    path ('inspiratie/termoformare/', views.termoformare, name='termoformare'),
    path ('inspiratie/printTextile/', views.print_pe_textile, name='print_pe_textile'),
    path ('inspiratie/firmeLuminoase/', views.firme_luminoase, name='firme_luminoase'),
    path ('inspiratie/timbruSec/', views.timbru_sec, name='timbru_sec'),
    path ('inspiratie/produsePromotionale/', views.produse_promotionale, name='produse_promotionale'),
    path ('utilaje/', views.Utilaje.as_view(), name='utilaje'),
    path ('preturi/', views.preturi, name='preturi'),
    path ('contact/', views.contact, name='contact'),
]

