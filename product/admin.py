from django.contrib import admin
from .models import Utilaj, UtilajDescription, UtilajImage, UtilajCaracteristici

# Register your models here.
admin.site.register(Utilaj)
admin.site.register(UtilajDescription)
admin.site.register(UtilajImage)
admin.site.register(UtilajCaracteristici)


