# Generated by Django 3.1.2 on 2021-03-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210302_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
