import peewee

db = peewee.SqliteDatabase("sante.db")

class Region(peewee.Model):
    nom = peewee.CharField(max_length=60)

    class Meta:
        database = db

class Hospital(peewee.Model):
    nom = peewee.CharField(max_length=60)
    region = peewee.ForeignKeyField(Region)

    class Meta:
        database = db

class HospitalRecord(peewee.Model):
    hospital = peewee.ForeignKeyField(Hospital)
    civieres_fonctionnelles = peewee.IntegerField()
    civieres_occupees = peewee.IntegerField()
    taux_occupation = peewee.DecimalField(max_digits=5, decimal_places=2)
    patients_plus_24 = peewee.IntegerField()
    patients_plus_48 = peewee.IntegerField()

    class Meta:
        database = db
