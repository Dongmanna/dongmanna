# Generated by Django 3.2.6 on 2021-08-08 13:18

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='post/images'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
