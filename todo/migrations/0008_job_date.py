# Generated by Django 4.1.2 on 2022-11-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_thought_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
