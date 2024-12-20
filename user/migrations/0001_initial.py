# Generated by Django 4.2.17 on 2024-12-15 17:36

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_office_staff', models.BooleanField(default=False)),
                ('is_librarian', models.BooleanField(default=False)),
                ('employee_id', models.CharField(blank=True, help_text='Unique ID for the librarian', max_length=50, null=True, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('landmark', models.CharField(blank=True, max_length=255, null=True)),
                ('place', models.CharField(blank=True, max_length=20, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=10, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, help_text='Monthly salary of the librarian', max_digits=10, null=True)),
                ('department', models.CharField(blank=True, help_text='Department the staff belongs to, e.g., Accounts, Admissions', max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='custom_user_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
