# Generated by Django 4.1.5 on 2023-02-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0003_alter_modelformwithfilefield_file_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelformwithfilefield",
            name="file_model",
            field=models.FileField(upload_to="uploads"),
        ),
    ]
