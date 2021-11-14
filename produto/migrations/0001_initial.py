# Generated by Django 3.2.7 on 2021-09-14 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('unidade_medida', models.CharField(choices=[('unidade', 'Unidade'), ('kilo', 'Kilo'), ('litro', 'Litro')], max_length=11, verbose_name='Unidade de medida')),
                ('quantidade_embalagem', models.IntegerField(verbose_name='Qantidade na embalagem')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='preço')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedor.fornecedor')),
            ],
            options={
                'ordering': ('produto',),
            },
        ),
    ]
