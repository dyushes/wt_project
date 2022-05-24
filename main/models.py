from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


class Citys(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    region = models.ForeignKey('Regions', models.DO_NOTHING, db_column='Region_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citys'
        verbose_name = 'city'
        verbose_name_plural = 'citys'

    def __str__(self):
        return self.name


class Countrys(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'countrys'
        verbose_name = 'country'
        verbose_name_plural = 'countrys'

    def __str__(self):
        return self.name


class Employer(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=256)  # Field name made lowercase.
    second_name = models.CharField(db_column='Second_Name', max_length=256)  # Field name made lowercase.
    city = models.ForeignKey(Citys, models.DO_NOTHING, db_column='City_id')  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employer'
        verbose_name = 'employer'
        verbose_name_plural = 'employers'

    def __str__(self):
        return self.name


class JobVacancy(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    owner = models.ForeignKey(Employer, models.DO_NOTHING, db_column='Owner_id')  # Field name made lowercase.
    addres = models.CharField(db_column='Addres', max_length=256)  # Field name made lowercase.
    city = models.ForeignKey(Citys, models.DO_NOTHING, db_column='City_id')  # Field name made lowercase.
    discription = models.CharField(db_column='Discription', max_length=256)  # Field name made lowercase.
    sellary = models.FloatField(db_column='Sellary')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'job_vacancy'
        verbose_name = 'job_vacancy'
        verbose_name_plural = 'job_vacancys'

    def __str__(self):
        return self.name


class Regions(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    country = models.ForeignKey(Countrys, models.DO_NOTHING, db_column='Country_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regions'
        verbose_name = 'region'
        verbose_name_plural = 'regions'

    def __str__(self):
        return self.name


class University(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    city = models.ForeignKey(Citys, models.DO_NOTHING, db_column='City_id')  # Field name made lowercase.
    addres = models.CharField(db_column='Addres', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'university'
        verbose_name = 'university'
        verbose_name_plural = 'universitys'

    def __str__(self):
        return self.name

class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    active = models.IntegerField()
    user_type = models.ForeignKey('UsersType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.name

class UsersType(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_type'

    def __str__(self):
        return self.name


class Workers(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    suename = models.CharField(db_column='Suename', max_length=256)  # Field name made lowercase.
    second_name = models.CharField(db_column='Second_name', max_length=256)  # Field name made lowercase.
    user = models.ForeignKey(Users, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    university = models.ForeignKey(University, models.DO_NOTHING, db_column='University_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workers'
        verbose_name = 'worker'
        verbose_name_plural = 'workers'

    def __str__(self):
        return self.name