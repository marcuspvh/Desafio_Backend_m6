# Generated by Django 4.1.5 on 2023-02-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0005_rename_cartão_transactions_cartao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactions",
            name="data",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="hora",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="tipo",
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="valor",
            field=models.IntegerField(),
        ),
    ]
