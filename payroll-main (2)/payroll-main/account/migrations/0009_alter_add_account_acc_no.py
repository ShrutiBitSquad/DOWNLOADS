# Generated by Django 4.2 on 2023-05-23 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_add_account_acc_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_account',
            name='acc_no',
            field=models.CharField(default=0, unique=True),
        ),
    ]
