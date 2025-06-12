from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import EquipoFutbol, Jugador, Campeonato, CampeonatoEquipos

@admin.register(EquipoFutbol)
class EquipoFutbolAdmin(ImportExportModelAdmin):
    pass

@admin.register(Jugador)
class JugadorAdmin(ImportExportModelAdmin):
    pass

@admin.register(Campeonato)
class CampeonatoAdmin(ImportExportModelAdmin):
    pass

@admin.register(CampeonatoEquipos)
class CampeonatoEquiposAdmin(ImportExportModelAdmin):
    pass
