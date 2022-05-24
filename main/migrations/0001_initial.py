# Generated by Django 4.0.4 on 2022-05-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citys',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=256)),
            ],
            options={
                'db_table': 'citys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Countrys',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=256)),
            ],
            options={
                'db_table': 'countrys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=256)),
                ('surname', models.CharField(db_column='Surname', max_length=256)),
                ('second_name', models.CharField(db_column='Second_Name', max_length=256)),
            ],
            options={
                'db_table': 'employer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JobVacancy',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=256)),
                ('addres', models.CharField(db_column='Addres', max_length=256)),
                ('discription', models.CharField(db_column='Discription', max_length=256)),
                ('sellary', models.FloatField(db_column='Sellary')),
            ],
            options={
                'db_table': 'job_vacancy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=256)),
            ],
            options={
                'db_table': 'regions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=256)),
                ('addres', models.CharField(db_column='Addres', max_length=256)),
            ],
            options={
                'db_table': 'university',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('active', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersType',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=256)),
            ],
            options={
                'db_table': 'users_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=256)),
                ('suename', models.CharField(db_column='Suename', max_length=256)),
                ('second_name', models.CharField(db_column='Second_name', max_length=256)),
            ],
            options={
                'db_table': 'workers',
                'managed': False,
            },
        ),
    ]
