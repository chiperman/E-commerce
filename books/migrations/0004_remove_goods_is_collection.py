# Generated by Django 3.0.8 on 2020-08-05 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200805_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='is_collection',
        ),
    ]