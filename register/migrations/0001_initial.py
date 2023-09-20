# Generated by Django 4.2.1 on 2023-05-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name="Ім'я")),
                ('email', models.CharField(max_length=250, verbose_name='Електронна адреса')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
            ],
        ),
    ]