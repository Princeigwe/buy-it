# Generated by Django 3.1.4 on 2021-03-22 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='telephone',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
