# Generated by Django 5.2 on 2025-04-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_tecnologias_empresa_logo_empresa_tecnologias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(null=True, upload_to='logo_empresa'),
        ),
    ]
