# Generated by Django 3.1.5 on 2021-01-23 22:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0003_auto_20210123_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='expens',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expens',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]