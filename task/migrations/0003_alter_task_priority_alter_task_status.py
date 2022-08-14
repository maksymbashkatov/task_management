# Generated by Django 4.0.6 on 2022-08-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('high', 'High'), ('medium', 'Medium')], default='Medium', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('todo', 'To do'), ('in_progress', 'In progress'), ('blocked', 'Blocked'), ('finished', 'Finished')], default='Low', max_length=20),
        ),
    ]