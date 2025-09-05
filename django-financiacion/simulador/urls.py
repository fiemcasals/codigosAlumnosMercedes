from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_financiacion, name="form_financiacion"),
]
