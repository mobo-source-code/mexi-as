# Generated by Django 4.0.3 on 2022-03-31 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0010_remove_takingarticles_poste_alter_taking_poste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]