# Generated by Django 3.1.2 on 2021-02-18 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputcs', '0011_auto_20210217_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ajaxd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=30)),
            ],
        ),
    ]
