# Generated by Django 3.0.14 on 2023-01-13 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_proposedtopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicname', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=30)),
                ('time', models.TimeField(max_length=30)),
                ('room', models.CharField(max_length=30)),
            ],
        ),
    ]
