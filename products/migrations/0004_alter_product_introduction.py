# Generated by Django 3.2.25 on 2024-03-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240318_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='introduction',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]