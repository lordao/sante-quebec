import inspect
import sys
from datetime import datetime

import peewee

db = peewee.SqliteDatabase("sante.db")


class Scrape(peewee.Model):
    scrape_date = peewee.DateTimeField(default=datetime.now())

    class Meta:
        database = db


class Region(peewee.Model):
    nom = peewee.CharField(max_length=60)
    scrape = peewee.ForeignKeyField(Scrape)

    class Meta:
        database = db


class Hospital(peewee.Model):
    nom = peewee.CharField(max_length=60)
    region = peewee.ForeignKeyField(Region)
    scrape = peewee.ForeignKeyField(Scrape)

    class Meta:
        database = db


class HospitalRecord(peewee.Model):
    hospital = peewee.ForeignKeyField(Hospital)
    civieres_fonctionnelles = peewee.IntegerField()
    civieres_occupees = peewee.IntegerField()
    taux_occupation = peewee.DecimalField(max_digits=5, decimal_places=2)
    patients_plus_24 = peewee.IntegerField()
    patients_plus_48 = peewee.IntegerField()
    scrape = peewee.ForeignKeyField(Scrape)

    class Meta:
        database = db


models = inspect.getmembers(sys.modules[__name__], inspect.isclass)
models = dict(models).values()
for model in models:
    try:
        model.create_table()
    except peewee.OperationalError:
        print("Table {} already exists!".format(model.__name__))
