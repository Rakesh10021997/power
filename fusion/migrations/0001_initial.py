# Generated by Django 3.1.1 on 2021-07-05 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dressname', models.CharField(default='', max_length=30, null=True)),
                ('rent_price', models.IntegerField()),
                ('rent_security', models.IntegerField()),
                ('size', models.CharField(default='', max_length=30, null=True)),
                ('product_name', models.CharField(default='', max_length=30, null=True)),
                ('product_id', models.CharField(default='', max_length=30, null=True)),
                ('color', models.CharField(default='', max_length=30, null=True)),
                ('materials', models.CharField(default='', max_length=30, null=True)),
                ('neckdesign', models.CharField(default='', max_length=30, null=True)),
                ('sleeves', models.CharField(default='', max_length=30, null=True)),
                ('designer', models.CharField(default='', max_length=30, null=True)),
            ],
        ),
    ]
