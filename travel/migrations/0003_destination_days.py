# Generated by Django 5.1.6 on 2025-02-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_destination_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='days',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
