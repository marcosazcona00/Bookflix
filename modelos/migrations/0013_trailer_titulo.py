# Generated by Django 3.0.5 on 2020-06-06 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0012_auto_20200606_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailer',
            name='titulo',
            field=models.CharField(default=None, max_length=255, unique=True),
        ),
    ]