# Generated by Django 3.1.3 on 2021-05-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat',
            field=models.TextField(),
        ),
    ]
