# Generated by Django 4.1.2 on 2022-11-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_thought_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='img',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
