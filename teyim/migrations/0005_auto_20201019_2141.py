# Generated by Django 3.1.2 on 2020-10-20 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teyim', '0004_auto_20201019_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/%Y/%m/%d/'),
        ),
    ]
