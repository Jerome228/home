# Generated by Django 3.1.5 on 2021-01-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0004_auto_20210123_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expens',
            name='comment',
            field=models.TextField(blank=True, max_length=512),
        ),
    ]
