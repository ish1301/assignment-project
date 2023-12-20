# Generated by Django 3.2.23 on 2023-12-20 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageupload',
            name='analysis',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='filename',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='md5_hash',
            field=models.CharField(max_length=32, null=True),
        ),
    ]