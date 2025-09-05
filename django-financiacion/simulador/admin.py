# simulador/admin.py
from django.contrib import admin
from .models import Simulacion

@admin.register(Simulacion)
class SimulacionAdmin(admin.ModelAdmin):
    list_display = ("id","monto_financiar","cuotas","interes_anual","sistema","cuota_mensual","created_at")
    list_filter = ("sistema","created_at")
    search_fields = ("id",)
