# Generated by Django 3.2.15 on 2022-09-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
                ('no_of_books', models.IntegerField(null=True)),
            ],
        ),
    ]