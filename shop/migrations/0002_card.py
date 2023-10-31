# Generated by Django 4.2.6 on 2023-10-31 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, verbose_name='Card number')),
                ('month', models.CharField(max_length=2, verbose_name='Month')),
                ('year', models.CharField(max_length=2, verbose_name='Year')),
                ('cvc', models.CharField(max_length=16, verbose_name='CVC')),
                ('card_name', models.CharField(max_length=64, verbose_name='Card name')),
            ],
        ),
    ]
