# Generated by Django 3.1.7 on 2021-03-16 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0006_auto_20200724_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='Company',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
