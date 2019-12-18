# Generated by Django 2.1.2 on 2019-11-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('address', models.TextField(max_length=100)),
            ],
        ),
    ]
