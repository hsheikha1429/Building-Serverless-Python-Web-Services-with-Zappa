# Generated by Django 2.0.3 on 2018-03-28 09:50

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20180317_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=gallery.models.upload_path, verbose_name='image'),
        ),
    ]
