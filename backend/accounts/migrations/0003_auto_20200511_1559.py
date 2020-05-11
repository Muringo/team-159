# Generated by Django 3.0.6 on 2020-05-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_business_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='Business/Images/')),
                ('certificate', models.FileField(upload_to='Business/Certificate/')),
            ],
        ),
        migrations.RemoveField(
            model_name='business',
            name='certificate',
        ),
        migrations.RemoveField(
            model_name='business',
            name='images',
        ),
    ]