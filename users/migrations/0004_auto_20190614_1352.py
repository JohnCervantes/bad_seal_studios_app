# Generated by Django 2.2.2 on 2019-06-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190613_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/default.jpg/', upload_to='images/'),
        ),
    ]
