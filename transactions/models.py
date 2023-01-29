from django.db import models
from django import forms



class ModelFormWithFileField(models.Model):
    file = models.FileField()

class UploadFileForm(forms.Form):
    file = forms.FileField()

class Transactions(models.Model):
    tipo = models.IntegerField()
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    cartão = models.CharField(max_length=20)
    hora = models.TimeField()
    representante = models.CharField(max_length=100)
    loja = models.CharField(max_length=100)
    




   