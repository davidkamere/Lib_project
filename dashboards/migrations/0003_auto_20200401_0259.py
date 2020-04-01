# Generated by Django 3.0.4 on 2020-03-31 23:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0002_auto_20200330_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowed',
            name='last_borrowed_on',
        ),
        migrations.AddField(
            model_name='borrowed',
            name='borrowed_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
