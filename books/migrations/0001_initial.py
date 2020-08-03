# Generated by Django 3.0.8 on 2020-07-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
