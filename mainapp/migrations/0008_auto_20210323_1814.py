# Generated by Django 3.1.7 on 2021-03-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210323_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(default='ТЕКСТ'),
        ),
    ]
