# Generated by Django 5.0 on 2024-01-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amStaticApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]