# Generated by Django 3.0.4 on 2020-04-01 09:07

import dashboards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0005_auto_20200401_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed',
            name='due_date',
            field=models.DateTimeField(blank=True, default=dashboards.models.get_due_date, null=True),
        ),
    ]
