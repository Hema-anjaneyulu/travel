# Generated by Django 2.2.6 on 2019-11-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_auto_20191106_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='desc',
            new_name='desc1',
        ),
        migrations.AddField(
            model_name='destination',
            name='desc5',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
