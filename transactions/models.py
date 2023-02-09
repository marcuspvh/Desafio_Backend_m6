from django.db import models
from django import forms



class ModelFormWithFileField(models.Model):
    file_model = models.FileField(upload_to='uploads')

class UploadFileForm(forms.Form):
    file = forms.FileField()

class Transactions(models.Model):
    tipo = models.CharField(max_length=13)
    data = models.CharField(max_length=10)
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=20)
    hora = models.CharField(max_length=10)
    dono = models.CharField(max_length=100)
    loja = models.CharField(max_length=100)
    




   