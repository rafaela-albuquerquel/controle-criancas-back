# Generated by Django 5.1.2 on 2024-11-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_crianca_nome_alter_responsavel_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='status',
            field=models.CharField(choices=[('checkin', 'Check-in'), ('checkout', 'Check-out')], default='checkin', max_length=10),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='telefone_responsavel',
            field=models.CharField(max_length=11),
        ),
    ]
