# Generated by Django 4.0.3 on 2022-06-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_alter_taking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='taking',
            name='total_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
