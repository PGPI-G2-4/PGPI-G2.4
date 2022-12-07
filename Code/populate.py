# PYTHON SCRIPT FOR IMPORTING CSV DATA INTO THE DATABASE
# Paths to the CSV files
from datetime import datetime


csv_paths = ["C:/Users/Usuario/Desktop/Universidad/4Cuarto/PGPI/Data/Departamentos.csv",
                "C:/Users/Usuario/Desktop/Universidad/4Cuarto/PGPI/Data/Medicos.csv",
                "C:/Users/Usuario/Desktop/Universidad/4Cuarto/PGPI/Data/User.csv",
             "C:/Users/Usuario/Desktop/Universidad/4Cuarto/PGPI/Data/Citas.csv"]
# Path to the directory for django.
djangoproject_home = "C:/Users/Usuario/Desktop/Universidad/4Cuarto/PGPI/PGPI-G2.4/Code"

import sys,os
sys.path.append(djangoproject_home)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from ecommerce.apps.account.models import *
from ecommerce.apps.catalogue.models import *
from ecommerce.apps.orders.models import *
from ecommerce.apps.checkout.models import *
from ecommerce.apps.orders.models import *



import csv
dataReader = csv.reader(open(csv_paths[0]), delimiter=';', quotechar='"')

for row in dataReader:
    if row[0] != 'name': # Ignore the header row, import everything else
        department = Department()
        department.name = row[0]
        department.save()

dataReader = csv.reader(open(csv_paths[1]), delimiter=';', quotechar='"')
for row in dataReader:
    if row[0] != 'name': # Ignore the header row, import everything else
        medic = Medic()
        medic.name = row[0]
        medic.surname = row[1]
        medic.image = row[2]
        medic.department = Department.objects.get(name=row[3])
        medic.id = row[4]
        medic.save()

dataReader = csv.reader(open(csv_paths[2]), delimiter=';', quotechar='"')
for row in dataReader:
    if row[0] != 'email': # Ignore the header row, import everything else
        user = Customer()
        user.email = row[0]
        user.password = row[1]
        user.first_name = row[2]
        user.last_name = row[3]
        user.age = row[4]
        user.gender = row[5]
        user.region = row[6]
        user.alergies = row[7]
        user.pathologies = row[8]
        user.username = row[9]
        user.id = row[10]
        user.save()

dataReader = csv.reader(open(csv_paths[3]), delimiter=';', quotechar='"')
for row in dataReader:
    if row[0] != 'date_time': # Ignore the header row, import everything else
        appoinment = Appointment()
        appoinment.date_time = row[0]
        appoinment.client_name = row[1]
        appoinment.client_surname = row[2]
        appoinment.client_email = row[3]
        appoinment.price = row[4]
        appoinment.id = row[5]
        appoinment.medic = Medic.objects.get(id=row[5])
        appoinment.save()


