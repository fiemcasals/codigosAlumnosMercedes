# simulador/forms.py
from decimal import Decimal
from django import forms

class SimulacionForm(forms.Form):
    monto_disponible = forms.DecimalField(
        label="Monto disponible",
        min_value=Decimal('0.00'),
        decimal_places=2,
        max_digits=12,
        widget=forms.NumberInput(attrs={"step":"0.01", "min":"0"})
    )
    monto_financiar = forms.DecimalField(
        label="Monto a financiar",
        min_value=Decimal('0.01'),
        decimal_places=2,
        max_digits=12,
        widget=forms.NumberInput(attrs={"step":"0.01", "min":"0.01"})
    )
    cuotas = forms.IntegerField(
        label="Cantidad de cuotas",
        min_value=1,
        widget=forms.NumberInput(attrs={"min":"1"})
    )
    interes_anual = forms.DecimalField(
        label="Interés anual (%)",
        min_value=Decimal('0.00'),
        decimal_places=2,
        max_digits=6,
        widget=forms.NumberInput(attrs={"step":"0.01", "min":"0"})
    )
    sistema = forms.ChoiceField(
        label="Sistema",
        choices=[("FR","Francés (cuota fija)")],  # podemos ampliar luego
        initial="FR"
    )
