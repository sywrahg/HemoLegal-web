# Generated by Django 2.0 on 2018-04-06 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_doacao', models.DateField(auto_now=True)),
                ('quant_bolsas', models.IntegerField()),
                ('direcionada', models.BooleanField()),
                ('paciente', models.CharField(max_length=30, verbose_name='paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='cpf')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1)),
                ('telefone', models.CharField(max_length=14, verbose_name='telefone')),
                ('dt_nascimento', models.DateField()),
                ('tipo_sangue', models.CharField(choices=[('ap', 'A+'), ('an', 'A-'), ('bp', 'B+'), ('bn', 'B-'), ('abp', 'AB+'), ('abn', 'AB-'), ('op', 'O+'), ('on', 'O-')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=50, verbose_name='logradouro')),
                ('numero', models.IntegerField()),
                ('estado', models.CharField(max_length=20, verbose_name='estado')),
                ('cidade', models.CharField(max_length=20, verbose_name='cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_sangue', models.CharField(choices=[('ap', 'A+'), ('an', 'A-'), ('bp', 'B+'), ('bn', 'B-'), ('abp', 'AB+'), ('abn', 'AB-'), ('op', 'O+'), ('on', 'O-')], max_length=3)),
                ('quant_bolsas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hemocentro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('telefone', models.CharField(max_length=14, verbose_name='telefone')),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hemocentro_endereco', to='core.Endereco')),
                ('estoque_sanguineo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meu_Estoque', to='core.Estoque')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('telefone', models.CharField(max_length=14, verbose_name='telefone')),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_endereco', to='core.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_sangue', models.CharField(choices=[('ap', 'A+'), ('an', 'A-'), ('bp', 'B+'), ('bn', 'B-'), ('abp', 'AB+'), ('abn', 'AB-'), ('op', 'O+'), ('on', 'O-')], max_length=3)),
                ('data_transacao', models.DateField(auto_now=True)),
                ('quant_bolsas', models.IntegerField()),
                ('emissor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repasses', to='core.Hemocentro')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recebidos', to='core.Hospital')),
            ],
        ),
        migrations.AddField(
            model_name='doador',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doador_endereco', to='core.Endereco'),
        ),
        migrations.AddField(
            model_name='doacao',
            name='doador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doacoes_realizadas', to='core.Doador'),
        ),
        migrations.AddField(
            model_name='doacao',
            name='hemocentro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doacoes_recebidas', to='core.Hemocentro'),
        ),
        migrations.AddField(
            model_name='doacao',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doacoes_direcionadas', to='core.Hospital'),
        ),
    ]
