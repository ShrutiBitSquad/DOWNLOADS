# Generated by Django 4.2 on 2023-05-19 09:47

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_no', models.IntegerField(default=0, unique=True)),
                ('ifsc', models.CharField(max_length=20)),
                ('current_bal', models.IntegerField(default=0)),
                ('current_due', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.IntegerField(default=0, unique=True)),
                ('bill_date', models.DateField()),
                ('bill_amount', models.IntegerField(default=0)),
                ('bill_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('pass', 'Pass'), ('fail', 'Fail')], default='pass', max_length=20)),
                ('notes', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Graduation_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem1', models.FileField(blank=True, null=True, upload_to='files')),
                ('sem2', models.FileField(blank=True, null=True, upload_to='files')),
                ('sem3', models.FileField(blank=True, null=True, upload_to='files')),
                ('sem4', models.FileField(blank=True, null=True, upload_to='files')),
                ('sem5', models.FileField(blank=True, null=True, upload_to='files')),
                ('sem6', models.FileField(blank=True, null=True, upload_to='files')),
                ('sem7', models.FileField(blank=True, null=True, upload_to='files')),
                ('sem8', models.FileField(blank=True, null=True, upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_no', models.IntegerField(default=0)),
                ('nominee', models.CharField(max_length=20)),
                ('insured_value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.IntegerField(default=0, unique=True)),
                ('invoice_date', models.DateField()),
                ('invoice_amount', models.IntegerField(default=0)),
                ('deduction', models.IntegerField(default=0)),
                ('deduction_reason', models.CharField(max_length=200)),
                ('received_transfer', models.CharField(choices=[('in', 'In'), ('out', 'Out')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Marksheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssc', models.FileField(blank=True, null=True, upload_to='files')),
                ('hsc', models.FileField(blank=True, null=True, upload_to='files')),
                ('graduation_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.graduation_details')),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column1', models.FileField(blank=True, null=True, upload_to='files')),
                ('column2', models.FileField(blank=True, null=True, upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('payment_ref_no', models.IntegerField(default=0, unique=True)),
                ('received_payment_transfer', models.CharField(choices=[('in', 'In'), ('out', 'Out')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PostGraduation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem1', models.FileField(blank=True, null=True, upload_to='files')),
                ('sem2', models.FileField(blank=True, null=True, upload_to='files')),
                ('sem3', models.FileField(blank=True, null=True, upload_to='files')),
                ('sem4', models.FileField(blank=True, null=True, upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('fathername', models.CharField(max_length=20)),
                ('mothername', models.CharField(max_length=20)),
                ('adhar_no', models.IntegerField(default=0)),
                ('adhar_attach', models.FileField(blank=True, null=True, upload_to='files')),
                ('pan_no', models.CharField(max_length=15)),
                ('pan_attach', models.FileField(blank=True, null=True, upload_to='files')),
                ('graduation', models.CharField(choices=[('ug', 'UG'), ('pg', 'PG')], default='ug', max_length=20)),
                ('dob', models.DateField()),
                ('doj', models.DateField()),
                ('probation_days', models.IntegerField(default=90)),
                ('evalution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.evaluation')),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.insurance')),
                ('marksheet_attach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.marksheet')),
            ],
        ),
        migrations.AddField(
            model_name='marksheet',
            name='post_graduation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.postgraduation'),
        ),
        migrations.CreateModel(
            name='Finance_out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('ref_no', models.IntegerField(default=0, unique=True)),
                ('tds_tax', models.IntegerField(default=0)),
                ('salary_process', models.CharField(max_length=20)),
                ('final', models.IntegerField(blank=True, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.add_account')),
                ('bills', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.bill')),
                ('invoice_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.invoice')),
                ('payment_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.payment')),
            ],
        ),
        migrations.CreateModel(
            name='Finance_in',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('ref_no', models.IntegerField(default=0, unique=True)),
                ('tds_tax', models.IntegerField(default=0)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.add_account')),
                ('invoice_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.invoice')),
                ('payment_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.payment')),
            ],
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mob', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('object_manager', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
