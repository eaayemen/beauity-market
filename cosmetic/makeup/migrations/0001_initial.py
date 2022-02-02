# Generated by Django 4.0.1 on 2022-01-30 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True,serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('expire_date', models.DateField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
