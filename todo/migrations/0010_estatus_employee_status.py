# Generated by Django 4.1.2 on 2022-11-18 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_strgtask_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('reason', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Estatus',
                'verbose_name_plural': 'Estatuss',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo.estatus'),
        ),
    ]