# Generated by Django 4.2 on 2023-05-22 07:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_usertable_firstname_alter_usertable_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9]+@[a-zA-Z0-9]+\\.[a-zA-Z]{2,}$', 'Enter a valid email address.')]),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='firstname',
            field=models.CharField(max_length=65, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets  are allowed.')]),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='lastname',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets  are allowed.')]),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='mob',
            field=models.CharField(max_length=25, validators=[django.core.validators.RegexValidator('^(\\+\\d{1,3})?\\d{"0-9"}$', 'Enter a valid mobile number.')]),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='password',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('[A-Za-z0-9@#$%^&+=]{6,}', message='Must have atleast one: A-Z,a-z,0-9,sp. character')]),
        ),
    ]
