# Generated by Django 2.2.2 on 2019-06-15 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_projects_technologies'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='carousel',
            field=models.CharField(default='default', max_length=300),
            preserve_default=False,
        ),
    ]