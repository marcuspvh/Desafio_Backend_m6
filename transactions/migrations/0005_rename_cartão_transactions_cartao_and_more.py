# Generated by Django 4.1.5 on 2023-02-08 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0004_alter_modelformwithfilefield_file_model"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transactions",
            old_name="cartão",
            new_name="cartao",
        ),
        migrations.RenameField(
            model_name="transactions",
            old_name="representante",
            new_name="dono",
        ),
    ]
