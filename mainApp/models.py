from django.db import models
from django.contrib.auth.models import User


class Suv(models.Model):
    brend = models.CharField(max_length=250)
    narx = models.PositiveIntegerField()
    litr = models.CharField(max_length=25)
    batafsil = models.CharField(max_length=250)


class Mijoz(models.Model):
    ism = models.CharField(max_length=250)
    tel = models.CharField(max_length=20)
    manzil = models.TextField()
    qarz = models.PositiveIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Admin(models.Model):
    ism = models.CharField(max_length=250)
    yosh = models.PositiveIntegerField()
    ish_vaqti = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Haydovchi(models.Model):
    ism = models.CharField(max_length=250)
    tel = models.CharField()
    kiritilgan_sana = models.DateField()

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    sana = models.DateTimeField()
    miqdor = models.CharField(max_length=250)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)

