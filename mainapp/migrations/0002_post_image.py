# Generated by Django 3.1.7 on 2021-02-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='static/media/picture/posts/<built-in function id>.png'),
        ),
    ]