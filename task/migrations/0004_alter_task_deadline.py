# Generated by Django 4.0.6 on 2022-08-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_task_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]