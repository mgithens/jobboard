# Generated by Django 5.0.6 on 2024-05-23 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='applied_at',
            new_name='applied_on',
        ),
    ]
