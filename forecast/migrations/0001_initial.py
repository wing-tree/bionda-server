# Generated by Django 4.2.4 on 2023-08-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nx', models.IntegerField()),
                ('ny', models.IntegerField()),
                ('response', models.JSONField()),
            ],
        ),
    ]