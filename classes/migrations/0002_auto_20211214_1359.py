# Generated by Django 3.0 on 2021-12-14 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='childagefinish',
            field=models.CharField(blank=True, help_text='When childagefinish there class', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='childagestart',
            field=models.CharField(blank=True, help_text='When childagestart there class', max_length=2, null=True),
        ),
    ]
