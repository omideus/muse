# Generated by Django 2.1.1 on 2018-09-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='museumobject',
            name='ded_id',
            field=models.IntegerField(null=True, verbose_name='شناسه شیء'),
        ),
    ]
