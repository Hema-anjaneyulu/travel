# Generated by Django 2.2.6 on 2019-11-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_auto_20191104_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='desc2',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='desc3',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='desc4',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
