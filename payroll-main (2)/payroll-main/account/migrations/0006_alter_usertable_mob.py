# Generated by Django 4.2 on 2023-05-22 09:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_add_account_acc_no_alter_add_account_ifsc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='mob',
            field=models.BigIntegerField(max_length=13, validators=[django.core.validators.RegexValidator('^[0-9]', 'Enter a valid mobile number.')]),
        ),
    ]