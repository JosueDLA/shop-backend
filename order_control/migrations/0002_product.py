# Generated by Django 3.1.4 on 2020-12-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]