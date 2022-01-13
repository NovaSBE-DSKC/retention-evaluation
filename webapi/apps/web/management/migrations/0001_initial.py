# Generated by Django 3.2 on 2021-04-13 15:35

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('S', 'Submision'), ('T', 'Training'), ('P', 'Problem'), ('R', 'Reset')], max_length=2)),
                ('description', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_data_uploaded', models.BooleanField(default=False)),
                ('data_file', models.FileField(null=True, upload_to='data/raw')),
                ('data_submission_timestamp', models.DateTimeField(null=True)),
                ('training', models.BooleanField(default=False)),
                ('trained', models.BooleanField(default=True)),
                ('last_train', models.DateTimeField(default=datetime.date(2020, 5, 14), null=True)),
                ('training_status', models.CharField(default='complete', max_length=120)),
            ],
        ),
    ]