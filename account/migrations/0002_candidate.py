# Generated by Django 4.1.5 on 2023-02-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=15)),
                ('lastName', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('desc', models.TextField(max_length=600)),
            ],
        ),
    ]
