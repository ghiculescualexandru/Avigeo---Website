from django.shortcuts import render
from .models import UtilajVanzare, UtilajPropriu, Firma
from django.views.generic import ListView

# Create your views here.

# VIEW PENTRU PAGINA HOME
def home(request):
    title = 'Home'
    has_footer = True

    return render(request, 'product/home.html', locals())


# VIEW PENTRU PAGINA DESPRENOI 
class DespreNoi(ListView):
    model = UtilajPropriu
    template_name = 'product/despre_noi.html'
    context_object_name = 'utilaje_proprii'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Despre Noi'
        context['has_footer'] = True

        return context

    # def get_queryset(self):
    #     queryset = UtilajVanzare.objects.all()

    #     return queryset


# VIEW PENTRU PAGINA INSPIRATIE
def inspiratie(request):
    title = 'Inspiratie'
    has_footer = True
    is_glider = True

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
    lightbox = True
    has_footer = True

    return render(request, 'product/printOutdoor.html', locals())

# VIEW PENTRU PAGINA PRINT INDOOR
def print_indoor(request):
    title = 'Print Indoor'
    lightbox = True
    has_footer = True

    return render(request, 'product/printIndoor.html', locals())

# VIEW PENTRU PAGINA TIPAR OFFSET
def tipar_offset(request):
    title = 'Tipar Offset'
    lightbox = True
    has_footer = True

    return render(request, 'product/tiparOffset.html', locals())

# VIEW PENTRU PAGINA LITERE VOLUMETRICE
def litere_volumetrice(request):
    title = 'Litere Volumetrice'
    lightbox = True
    has_footer = True

    return render(request, 'product/litereVolumetrice.html', locals())

# VIEW PENTRU PAGINA TERMOFORMARE
def termoformare(request):
    title = 'Termoformare'
    lightbox = True
    has_footer = True

    return render(request, 'product/termoformare.html', locals())

# VIEW PENTRU PAGINA PRINT PE TEXTILE
def print_pe_textile(request):
    title = 'Print Pe Textile'
    lightbox = True
    has_footer = True

    return render(request, 'product/printTextile.html', locals())

# VIEW PENTRU PAGINA FIRME LUMINOASE
def firme_luminoase(request):
    title = 'Firme Luminoase'
    has_footer = True    
    lightbox = True


    return render(request, 'product/firmeLuminoase.html', locals())

# VIEW PENTRU PAGINA TIMBRU SEC
def timbru_sec(request):
    title = 'Timbru Sec'
    lightbox = True
    has_footer = True

    return render(request, 'product/timbruSec.html', locals())

# VIEW PENTRU PAGINA PRODUSE PROMOTIONALE
def produse_promotionale(request):
    title = 'Produse Promotionale'
    lightbox = True
    has_footer = True

    return render(request, 'product/produsePromotionale.html', locals())

# VIEW PENTRU PAGINA UTILAJE
class Utilaje(ListView):
    model = Firma
    template_name = 'product/utilaje.html'
    context_object_name = 'firme'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Utilaje'
        context['has_footer'] = True
        context['is_glider'] = True
        context['is_full_glider'] = True

        return context

    # def get_queryset(self):
    #     queryset = UtilajPropriu.objects.all()

    #     return queryset

# VIEW PENTRU PAGINA PRETURI
def preturi(request):
    title = 'Preturi'
    has_footer = True

    return render(request, 'product/oferte.html', locals())

# VIEW PENTRU PAGINA CONTACT
def contact(request):
    title = 'Contact'
    has_footer = False

    return render(request, 'product/contact.html', locals())

# SFARSIT