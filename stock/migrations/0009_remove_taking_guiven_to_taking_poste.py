# Generated by Django 4.0.3 on 2022-03-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_article_single_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taking',
            name='guiven_to',
        ),
        migrations.AddField(
            model_name='taking',
            name='poste',
            field=models.CharField(blank=True, choices=[('CAFE', 'CAFE'), ('RESTAURENT', 'RESTAURENT'), ('LAITERIE', 'LAITERIE'), ('GRILLADE', 'GRILLADE'), ('TAFERNOUTE', 'TAFERNOUTE'), ('SNACK', 'SNACK')], max_length=125, null=True, verbose_name='Donnée à qui ?'),
        ),
    ]