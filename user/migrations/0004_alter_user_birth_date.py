# Generated by Django 4.1.3 on 2022-11-18 12:54

from django.db import migrations, models
import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_birth_date_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(validators=[user.validators.check_birth_date]),
        ),
    ]
