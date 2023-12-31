# Generated by Django 4.2 on 2023-05-23 06:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_add_account_acc_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_account',
            name='acc_no',
            field=models.BigIntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='add_account',
            name='current_bal',
            field=models.CharField(default=0),
        ),
        migrations.AlterField(
            model_name='add_account',
            name='current_due',
            field=models.CharField(default=0),
        ),
        migrations.AlterField(
            model_name='add_account',
            name='ifsc',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_amount',
            field=models.IntegerField(default=0, validators=[django.core.validators.RegexValidator('^[0-9]{0,12}$')]),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_date',
            field=models.DateField(validators=[django.core.validators.RegexValidator('^(\\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\\d|3[0-1])$')]),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_no',
            field=models.IntegerField(default=0, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_type',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets  are allowed.')]),
        ),
        migrations.AlterField(
            model_name='finance_in',
            name='amount',
            field=models.BigIntegerField(default=0, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{0,12}$')]),
        ),
        migrations.AlterField(
            model_name='finance_in',
            name='ref_no',
            field=models.IntegerField(default=0, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='finance_in',
            name='tds_tax',
            field=models.IntegerField(default=0, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='deduction',
            field=models.BigIntegerField(default=0, validators=[django.core.validators.RegexValidator('^(?!0\\.00)\\d{1,3}(?:,?\\d{3})*(?:\\.\\d{2})?$')]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='deduction_reason',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets  are allowed.')]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_amount',
            field=models.BigIntegerField(default=0, validators=[django.core.validators.RegexValidator('^(?!0\\.00)\\d{1,3}(?:,?\\d{3})*(?:\\.\\d{2})?$')]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(validators=[django.core.validators.RegexValidator('^(\\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\\d|3[0-1])$')]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(validators=[django.core.validators.RegexValidator('^(\\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\\d|3[0-1])$')]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_ref_no',
            field=models.IntegerField(default=0, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='adhar_no',
            field=models.BigIntegerField(default=0, validators=[django.core.validators.RegexValidator('^\\d{12,16}$')]),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='dob',
            field=models.DateField(validators=[django.core.validators.RegexValidator('^(\\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\\d|3[0-1])$')]),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='doj',
            field=models.DateField(validators=[django.core.validators.RegexValidator('^(\\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\\d|3[0-1])$')]),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='fathername',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets  are allowed.')]),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='firstname',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets  are allowed.')]),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='lastname',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets  are allowed.')]),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='mothername',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets  are allowed.')]),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='pan_no',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[A-Z]{5}[0-9]{4}[A-Z]{1}$')]),
        ),
    ]
