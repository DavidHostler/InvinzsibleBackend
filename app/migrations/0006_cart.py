# Generated by Django 3.1.2 on 2021-10-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(default='NA', max_length=150)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cart_details',
            },
        ),
    ]
