# Generated by Django 2.0.6 on 2018-06-27 07:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0002_auto_20180627_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='enq_date_end',
            field=models.DateField(default=datetime.datetime(2018, 7, 5, 7, 9, 16, 390222, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='enq_date_start',
            field=models.DateField(default=datetime.datetime(2018, 6, 28, 7, 9, 16, 390171, tzinfo=utc)),
        ),
    ]
