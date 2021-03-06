# Generated by Django 2.0.3 on 2018-04-10 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doador',
            old_name='tipo_sangue',
            new_name='sangue',
        ),
        migrations.AlterField(
            model_name='hemocentro',
            name='estoque_sanguineo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meu_estoque', to='core.Estoque'),
        ),
    ]
