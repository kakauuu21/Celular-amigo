# Generated by Django 5.1.2 on 2024-11-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]