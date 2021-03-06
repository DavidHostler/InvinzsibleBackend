# Generated by Django 3.1.2 on 2021-10-03 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211001_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('customer_id', models.CharField(max_length=15)),
                ('payment', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
            ],
            options={
                'db_table': 'order_details',
            },
        ),
    ]
