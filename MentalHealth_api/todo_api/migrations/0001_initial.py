# Generated by Django 4.1.1 on 2022-09-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('workout', models.CharField(max_length=32)),
                ('time', models.CharField(max_length=32)),
            ],
        ),
    ]
