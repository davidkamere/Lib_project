# Generated by Django 3.0.4 on 2020-04-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_collection', '0005_auto_20200401_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.IntegerField(choices=[(1, 'Available'), (2, 'Borrowed'), (3, 'Reserved')], default=1),
        ),
    ]