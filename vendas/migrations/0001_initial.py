# Generated by Django 2.2.3 on 2019-08-03 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=5)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('desconto', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('impostos', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('nfe_emitida', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('AB', 'Aberta'), ('FC', 'Fechada'), ('PC', 'Processando'), ('DC', 'Desconhecido')], default='DC', max_length=2)),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Person')),
            ],
            options={
                'permissions': (('setar_nfe', 'Usuario pode setar NF-e'), ('ver_dashboard', 'Pode visualizar dashboard')),
            },
        ),
        migrations.CreateModel(
            name='ItemDoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField()),
                ('desconto', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.Venda')),
            ],
            options={
                'verbose_name': 'Item do pedido',
                'verbose_name_plural': 'Itens do pedido',
                'unique_together': {('venda', 'produto')},
            },
        ),
    ]