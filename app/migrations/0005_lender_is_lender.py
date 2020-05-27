# Generated by Django 3.0.6 on 2020-05-21 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='lender',
            name='is_lender',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
