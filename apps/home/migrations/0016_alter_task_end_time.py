# Generated by Django 4.2.2 on 2023-07-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_alter_task_end_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="end_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
