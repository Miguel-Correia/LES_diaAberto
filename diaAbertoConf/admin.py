from django.contrib import admin

from .models import Transporte, Ementa, HorarioTransporte, TransporteUniversitarioHorario

# Register your models here.

admin.site.register(Transporte)
admin.site.register(HorarioTransporte)
admin.site.register(TransporteUniversitarioHorario)
admin.site.register(Ementa)
