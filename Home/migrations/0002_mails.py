# Generated by Django 5.1.3 on 2025-02-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('sna', models.AutoField(primary_key=True, serialize=False)),
                ('Locations', models.CharField(default=' ', max_length=500)),
                ('mails', models.CharField(max_length=500)),
            ],
        ),
    ]
