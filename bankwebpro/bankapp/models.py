from django.db import models

# Create your models here.
SEL_DIS=[('kozhikode','malappuram'),('eranakulam','kannur'),('wayanad','palakkad')]

SEL_BRAN=[('ramanatukara','omassery'),('thamarassery','aluva'),('vythiri','thalassery',)]

METERIAL=[('debitcard','creditcard')]

class person(models.Model):
    name= models.CharField(max_length=222)
    Dob= models.DateField()
    age= models.IntegerField()
    gender= models.CharField(max_length=100)
    phone= models.IntegerField()
    address= models.CharField(max_length=225)
    districts=models.CharField(max_length=15,choices=SEL_DIS,default='kannur')
    branches= models.CharField(max_length=15,choices=SEL_BRAN,default='ramanatukara')
    Acctype=models.CharField(max_length=200)
    meterialprovide=models.CharField(max_length=20,choices=METERIAL,default='debitcard')