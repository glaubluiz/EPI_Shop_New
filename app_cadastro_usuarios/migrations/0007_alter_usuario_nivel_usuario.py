# Generated by Django 4.2.16 on 2024-10-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuarios', '0006_alter_usuario_nivel_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nivel_usuario',
            field=models.CharField(choices=[('Cliente', 'Cliente'), ('Administrador', 'Administrador')], default='Cliente', max_length=15),
        ),
    ]
