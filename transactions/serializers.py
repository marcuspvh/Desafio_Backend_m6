from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Transactions
import ipdb

class TrasactionSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Transactions
        fields = [ 
        "tipo",
        "data",
        "valor",
        "cpf",
        "cartão",
        "hora",
        "representante",
        "loja",
        
        ]
        
        
    def create(self,  validated_data: dict) -> Transactions:
      
        transactions_obj = Transactions.objects.create(**validated_data)
        return transactions_obj
    
     





    
    # def handle_uploaded_file(f):
    #     with open('some/file/CNAB.txt', 'wb+') as destination:
    #         for chunk in f.chunks():
    #             destination.write(chunk)
   
       
       
       
       
       
       
     