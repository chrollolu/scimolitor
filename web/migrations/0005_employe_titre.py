# Generated by Django 4.1.7 on 2023-03-18 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_employe'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='titre',
            field=models.CharField(default='Mr', max_length=10),
            preserve_default=False,
        ),
    ]
