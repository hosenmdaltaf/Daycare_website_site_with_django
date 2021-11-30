# Generated by Django 3.0 on 2021-11-28 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField()),
                ('phonenumber', models.CharField(max_length=13)),
                ('Servicesname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Services')),
            ],
        ),
    ]
