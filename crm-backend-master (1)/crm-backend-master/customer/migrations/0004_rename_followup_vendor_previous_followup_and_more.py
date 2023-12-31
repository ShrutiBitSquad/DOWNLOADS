# Generated by Django 4.1.5 on 2023-07-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_followup_alter_vendor_followup_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='followup',
            new_name='previous_followup',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='nda_reason',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=20, null=True),
        ),
    ]
