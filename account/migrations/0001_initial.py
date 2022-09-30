# Generated by Django 3.2.4 on 2022-09-30 00:21

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('user_name', models.CharField(max_length=150, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='First_Name')),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='About')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name='Phone_Number')),
                ('postal_code', models.CharField(blank=True, max_length=12, verbose_name='Poastal_code')),
                ('address_line_1', models.CharField(blank=True, max_length=150, verbose_name='Address_line_1')),
                ('address_line_2', models.CharField(blank=True, max_length=150, verbose_name='Address_line_2')),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Accounts',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
