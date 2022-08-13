# Generated by Django 4.0.6 on 2022-08-12 15:34

from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_customuser_is_blocked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
            ],
            options={
                'verbose_name': 'User dashboard',
                'verbose_name_plural': 'Users dashboard',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.customuser',),
            managers=[
                ('objects', user.models.CustomUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_confirmed',
        ),
    ]
