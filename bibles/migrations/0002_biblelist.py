# Generated by Django 3.2 on 2022-02-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bibleList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]