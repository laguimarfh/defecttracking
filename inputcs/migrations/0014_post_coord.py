# Generated by Django 3.1.2 on 2021-02-18 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputcs', '0013_auto_20210217_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='coord',
            field=models.TextField(default='12'),
            preserve_default=False,
        ),
    ]