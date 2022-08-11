# Generated by Django 4.0.6 on 2022-08-10 19:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BNDESIntegration', '0017_alter_archivebndesoperacoes_delete_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivebndesoperacoes',
            name='delete_data',
            field=models.DateField(default=datetime.datetime(2022, 8, 10, 16, 14, 21, 692627)),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='data_search',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 10, 19, 14, 21, 691497, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='validity_day',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 9, 19, 14, 21, 691523, tzinfo=utc)),
        ),
    ]
