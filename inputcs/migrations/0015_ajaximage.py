# Generated by Django 3.1.2 on 2021-02-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputcs', '0014_post_coord'),
    ]

    operations = [
        migrations.CreateModel(
            name='AjaxImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_coord', models.JSONField()),
            ],
        ),
    ]
