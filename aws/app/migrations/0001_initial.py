# Generated by Django 3.1 on 2020-09-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userupdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile', models.IntegerField(blank=True, max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='media/')),
            ],
            options={
                'db_table': 'userdetails',
            },
        ),
    ]
