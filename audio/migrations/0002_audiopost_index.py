# Generated by Django 2.1.5 on 2019-05-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiopost',
            name='index',
            field=models.TextField(null=True),
        ),
    ]
