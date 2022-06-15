# Generated by Django 4.0.3 on 2022-03-23 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('nom', models.CharField(max_length=125, verbose_name="Nom de l'article")),
                ('group', models.CharField(max_length=125, verbose_name='Classification')),
                ('fourni', models.CharField(max_length=125, verbose_name='Fournisseur')),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='Prix Unitaire')),
                ('qte', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='Quantité En Stock')),
                ('ref', models.CharField(blank=True, max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Taking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('guiven_to', models.CharField(blank=True, max_length=125, verbose_name='Donnée à qui ?')),
                ('made_on', models.DateTimeField(auto_now=True, verbose_name='Date et heure de sortie')),
                ('ref', models.CharField(blank=True, max_length=125, verbose_name='Référence unique')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TakingArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.DecimalField(decimal_places=2, max_digits=12)),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.article')),
                ('taking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_sortant', to='stock.taking')),
            ],
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('qté', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Quantité Entrée')),
                ('fed_on', models.DateTimeField(auto_now_add=True, verbose_name='Fait le')),
                ('ref', models.CharField(blank=True, max_length=125, verbose_name='Référence unique')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeding', to='stock.article', verbose_name='Article à Entrant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
