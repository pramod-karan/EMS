# Generated by Django 3.2.12 on 2022-05-30 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_alter_employee_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
