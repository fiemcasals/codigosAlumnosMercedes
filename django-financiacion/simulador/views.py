# simulador/views.py
from decimal import Decimal, getcontext, ROUND_HALF_UP
from django.shortcuts import render
from .forms import SimulacionForm
from .models import Simulacion

getcontext().prec = 28  # precisión alta para potencias

def _redondear_moneda(x: Decimal) -> Decimal:
    return x.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def _calcular_frances(P: Decimal, n: int, interes_anual: Decimal):
    """
    Sistema francés (cuota fija).
    i_m = (interes_anual/100)/12 (nominal mensual)
    cuota = P * i_m / (1 - (1 + i_m)^(-n))
    Casos borde: i_m = 0 => cuota = P/n
    """
    i_m = (interes_anual / Decimal('100')) / Decimal('12')
    if i_m == 0:
        cuota = (P / Decimal(n))
    else:
        uno_mas_i = (Decimal('1') + i_m)
        cuota = P * i_m / (Decimal('1') - (uno_mas_i ** Decimal(-n)))
    cuota = _redondear_moneda(cuota)
    total = _redondear_moneda(cuota * n)
    intereses = _redondear_moneda(total - P)
    return (i_m, cuota, intereses, total)

def form_financiacion(request):
    contexto = {"resultado": None, "guardado": None}
    if request.method == 'POST':
        form = SimulacionForm(request.POST)
        if form.is_valid():
            monto_disponible = form.cleaned_data['monto_disponible']
            monto_financiar  = form.cleaned_data['monto_financiar']
            cuotas           = form.cleaned_data['cuotas']
            interes_anual    = form.cleaned_data['interes_anual']
            sistema          = form.cleaned_data['sistema']

            # Hoy sólo implementamos Francés
            i_m, cuota, intereses, total = _calcular_frances(
                P=monto_financiar, n=cuotas, interes_anual=interes_anual
            )

            # Guardamos en la BD
            sim = Simulacion.objects.create(
                monto_disponible=monto_disponible,
                monto_financiar=monto_financiar,
                cuotas=cuotas,
                interes_anual=interes_anual,
                sistema=sistema,
                tasa_mensual=i_m,
                cuota_mensual=cuota,
                total_intereses=intereses,
                total_a_pagar=total,
            )

            contexto["resultado"] = {
                "monto_disponible": monto_disponible,
                "monto_financiar":  monto_financiar,
                "cuotas":           cuotas,
                "interes_anual":    interes_anual,
                "sistema":          sistema,
                "tasa_mensual":     i_m,
                "cuota_mensual":    cuota,
                "total_intereses":  intereses,
                "total_a_pagar":    total,
            }
            contexto["guardado"] = sim.id
        else:
            contexto["errores"] = form.errors
    else:
        form = SimulacionForm()

    contexto["form"] = form
    return render(request, 'simulador/form.html', contexto)
