# Generated by Django 3.0.8 on 2020-07-31 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusMeetups', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buildings',
            options={'verbose_name_plural': 'Buildings'},
        ),
        migrations.AlterModelOptions(
            name='meetups',
            options={'verbose_name_plural': 'Meetups'},
        ),
        migrations.AlterModelOptions(
            name='meetuptypes',
            options={'verbose_name_plural': 'MeetupTypes'},
        ),
        migrations.AlterModelOptions(
            name='subjecttypes',
            options={'verbose_name_plural': 'SubjectTypes'},
        ),
    ]
