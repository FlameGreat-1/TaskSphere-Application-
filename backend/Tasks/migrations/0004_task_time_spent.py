# Generated by Django 5.1.2 on 2024-10-31 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0003_task_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_spent',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
