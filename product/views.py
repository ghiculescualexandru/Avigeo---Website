from django.shortcuts import render
from .models import Utilaj
from django.views.generic import ListView

# Create your views here.

# VIEW PENTRU PAGINA HOME
def home(request):
    title = 'Home'
    has_footer = True

    return render(request, 'product/home.html', locals())


# VIEW PENTRU PAGINA DESPRENOI 
class DespreNoi(ListView):
    model = Utilaj
    template_name = 'product/despre_noi.html'
    context_object_name = 'utilaje'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Despre Noi'
        context['has_footer'] = True

        return context

    def get_queryset(self):
        queryset = Utilaj.objects.filter(for_sale=False)

        return queryset


# VIEW PENTRU PAGINA INSPIRATIE
def inspiratie(request):
    title = 'Inspiratie'
    has_footer = True

    return render(request, 'product/catalog.html', locals())

# VIEW PENTRU PAGINA TIPAR DIGITAL
def tipar_digital(request):
    title = 'Tipar Digital'
    lightbox = True
    has_footer = True

    return render(request, 'product/tiparDigital.html', locals())

# VIEW PENTRU PAGINA PRINT OUTDOOR
def print_outdoor(request):
    title = 'Print Outdoor'
    has_footer = True

    return render(request, 'product/inspiratie/printOutdoor.html', locals())

# VIEW PENTRU PAGINA PRINT INDOOR
def print_indoor(request):
    title = 'Print Indoor'
    has_footer = True

    return render(request, 'product/inspiratie/printIndoor.html', locals())

# VIEW PENTRU PAGINA TIPAR OFFSET
def tipar_offset(request):
    title = 'Tipar Offset'
    has_footer = True

    return render(request, 'product/inspiratie/tiparOffset.html', locals())

# VIEW PENTRU PAGINA LITERE VOLUMETRICE
def litere_volumetrice(request):
    title = 'Litere Volumetrice'
    has_footer = True

    return render(request, 'product/inspiratie/litereVolumetrice.html', locals())

# VIEW PENTRU PAGINA TERMOFORMARE
def termoformare(request):
    title = 'Termoformare'
    has_footer = True

    return render(request, 'product/inspiratie/termoformare.html', locals())

# VIEW PENTRU PAGINA PRINT PE TEXTILE
def print_pe_textile(request):
    title = 'Print Pe Textile'
    has_footer = True

    return render(request, 'product/inspiratie/printTextile.html', locals())

# VIEW PENTRU PAGINA FIRME LUMINOASE
def firme_luminoase(request):
    title = 'Firme Luminoase'
    has_footer = True

    return render(request, 'product/inspiratie/firmeLuminoase.html', locals())

# VIEW PENTRU PAGINA TIMBRU SEC
def timbru_sec(request):
    title = 'Timbru Sec'
    has_footer = True

    return render(request, 'product/inspiratie/timbruSec.html', locals())

# VIEW PENTRU PAGINA PRODUSE PROMOTIONALE
def produse_promotionale(request):
    title = 'Produse Promotionale'
    has_footer = True

    return render(request, 'product/inspiratie/produsePromotionale.html', locals())

# VIEW PENTRU PAGINA UTILAJE
class Utilaje(ListView):
    model = Utilaj
    template_name = 'product/utilaje.html'
    context_object_name = 'utilaje'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Utilaje'
        context['has_footer'] = True

        return context

    def get_queryset(self):
        queryset = Utilaj.objects.filter(for_sale=True)

        return queryset

# VIEW PENTRU PAGINA PRETURI
def preturi(request):
    title = 'Preturi'
    has_footer = True

    return render(request, 'product/preturi.html', locals())

# VIEW PENTRU PAGINA CONTACT
def contact(request):
    title = 'Contact'
    has_footer = False

    return render(request, 'product/contact.html', locals())

# SFARSIT