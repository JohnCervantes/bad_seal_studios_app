# Generated by Django 2.2.2 on 2019-06-15 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20190615_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='carousel',
            field=models.TextField(null=True),
        ),
    ]
