# Generated by Django 4.0.3 on 2022-03-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_article_fourni_alter_article_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='takingarticles',
            name='poste',
            field=models.CharField(choices=[('CAFE', 'CAFE'), ('RESTAURENT', 'RESTAURENT'), ('LAITERIE', 'LAITERIE'), ('GRILLADE', 'GRILLADE'), ('TAFERNOUTE', 'TAFERNOUTE'), ('SNACK', 'SNACK')], max_length=125, null=True),
        ),
    ]
