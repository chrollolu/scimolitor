# Generated by Django 4.1.7 on 2023-03-18 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_employe_fonction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='prenoms',
        ),
    ]