# Generated by Django 3.2.6 on 2021-08-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='username',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
