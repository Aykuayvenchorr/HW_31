# Generated by Django 4.1.3 on 2022-11-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_ad_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
