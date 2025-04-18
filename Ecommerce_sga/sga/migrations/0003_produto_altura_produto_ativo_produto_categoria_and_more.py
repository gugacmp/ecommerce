# Generated by Django 5.2 on 2025-04-07 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0002_notafiscal'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='altura',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='codigo',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='comprimento',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='destaque',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='produto',
            name='largura',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='preco_promocional',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='sku',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='cor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tamanho',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
