# Generated by Django 3.0.4 on 2020-03-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='姓名')),
                ('date', models.DateField(verbose_name='日期')),
                ('temperture', models.CharField(default='正常', max_length=20, verbose_name='温度')),
            ],
        ),
    ]
