# Generated by Django 4.1.2 on 2022-11-19 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_alter_job_empid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='empid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo.employee'),
        ),
    ]