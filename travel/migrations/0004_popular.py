# Generated by Django 5.1.6 on 2025-02-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_destination_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
    ]
