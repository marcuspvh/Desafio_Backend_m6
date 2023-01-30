from rest_framework.views import APIView, Response, Request, status
from .models import ModelFormWithFileField
from rest_framework_simplejwt.authentication import JWTAuthentication
# from .serializers import handle_uploaded_file
from rest_framework import generics
from django.shortcuts import render, redirect
from .models import Transactions, UploadFileForm, ModelFormWithFileField
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponseRedirect
import ipdb




def upload_file(request):
        
        # if request.method == 'POST':
        #     form =ModelFormWithFileField(request.POST, request.FILES)
        #     ipdb.set_trace()
        #     file = form.file

     
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES['file']
                file_model = ModelFormWithFileField.objects.create(file_model='file')
                # ipdb.set_trace()    
                file_model.save()

            with open(request.FILES['file'].temporary_file_path(), 'r') as f:
            
                for data_form_line in file_model:
                    tipo = data_form_line[:1]
                    ano = data_form_line[1:5]
                    mes = data_form_line[5:7]
                    dia = data_form_line[7:9]
                    valor = data_form_line[9:19]
                    cpf = data_form_line[19:30]
                    cartao = data_form_line[30:42]
                    hora = data_form_line[42:44]
                    minuto = data_form_line[44:46]
                    segundo = data_form_line[46:48]
                    dono = data_form_line[48:62]
                    loja = data_form_line[62:81]
                    data = f"{dia}/{mes}/{ano}"
                    valor = int(valor) / 100
                    horario = f"{hora}:{minuto}:{segundo}"
                    if tipo == "1":
                        tipo = "Débito"
                    elif tipo == "2":
                        tipo = "Boleto"
                    elif tipo == "3":
                        tipo = "Financiamento"
                    elif tipo == "4":
                        tipo = "Crédito"
                    elif tipo == "5":
                        tipo = "Empréstimo"
                    elif tipo == "6":
                        tipo = "Vendas"
                    elif tipo == "7":
                        tipo = "TED"
                    elif tipo == "8":
                        tipo = "DOC"
                    elif tipo == "9":
                        tipo = "Aluguel"
                table_header = Transactions.objects.create(
                tipo=tipo,
                data=data,
                valor=valor,
                cpf=cpf,
                cartao=cartao,
                hora=horario,
                dono=dono,
                loja=loja,
                )
                table_header.save()
                
                amount_acount_store = Transactions.objects.values(
                    "tipo", "valor", "data", "cpf", "hora", "dono", "loja"
                )
                saldo_total = 0
                for operation in amount_acount_store:
                    if (
                        operation["tipo"] == "Boleto"
                        or operation["tipo"] == "Financiamento"
                        or operation["tipo"] == "Aluguel"
                    ):
                    
                        balance -= operation["valor"]
                    else:
                        balance += operation["valor"]
                return render(
                
                request,
                "reportCNAB.html",
                context={"amount_acount_store": amount_acount_store, "balance": balance},
            )
  
        else:
            form = UploadFileForm()
        return render(request, 'upload.html', {"form": form})











# class TransactionsView(APIView):
#     def get(self, request: Request) -> Response:
#         transactions = Transactions.objects.all()
#         serializer = TrasactionSerializer(transactions, many=True)
#         return Response(serializer.data)
    

#     def post(self, request: Request) -> Response:
#         serializer = TrasactionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)