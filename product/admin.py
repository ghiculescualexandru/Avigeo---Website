from django.contrib import admin
from .models import UtilajPropriu, UtilajVanzare, UtilajPropriuDescription, UtilajVanzareDescription, UtilajVanzareImage, Firma

# Register your models here.
admin.site.register(UtilajPropriu)
admin.site.register(UtilajVanzare)
admin.site.register(UtilajPropriuDescription)
admin.site.register(UtilajVanzareDescription)
admin.site.register(UtilajVanzareImage)
admin.site.register(Firma)



