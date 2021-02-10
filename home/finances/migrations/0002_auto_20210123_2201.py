# Generated by Django 3.1.5 on 2021-01-23 22:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expens',
            options={'ordering': ['amount'], 'verbose_name_plural': 'Expenses'},
        ),
        migrations.AddField(
            model_name='expens',
            name='comment',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='expens',
            name='amount',
            field=models.IntegerField(verbose_name='Montant'),
        ),
        migrations.AlterField(
            model_name='expens',
            name='ddate',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='expens',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Responsable de la dépense'),
        ),
        migrations.AlterField(
            model_name='expens',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Motif'),
        ),
    ]