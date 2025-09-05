# simulador/models.py
from django.db import models

class Simulacion(models.Model):
    SISTEMAS = [
        ('FR', 'Francés (cuota fija)'),
        # En el futuro podés agregar: ('AM', 'Americano'), ('AL', 'Alemán')
    ]

    # Entradas
    monto_disponible = models.DecimalField(max_digits=12, decimal_places=2)
    monto_financiar  = models.DecimalField(max_digits=12, decimal_places=2)
    cuotas           = models.PositiveIntegerField()
    interes_anual    = models.DecimalField(max_digits=6, decimal_places=2)  # % anual
    sistema          = models.CharField(max_length=2, choices=SISTEMAS, default='FR')

    # Salidas (resultados)
    tasa_mensual     = models.DecimalField(max_digits=10, decimal_places=8)  # i mensual (nominal)
    cuota_mensual    = models.DecimalField(max_digits=12, decimal_places=2)
    total_intereses  = models.DecimalField(max_digits=12, decimal_places=2)
    total_a_pagar    = models.DecimalField(max_digits=12, decimal_places=2)

    created_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sim #{self.id} — {self.cuotas} cuotas @ {self.interes_anual}%"
