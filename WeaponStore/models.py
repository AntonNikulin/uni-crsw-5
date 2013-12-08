from django.db import models
# -*- coding: utf-8 -*-
from time import time

def getUploadFileName(instance, filename):
    return "%s_%s" % (str(time()).replace('.','_'), str(filename))

class Item(models.Model):
    fullName = models.CharField(max_length=200, blank=True)
    shortName = models.CharField(max_length=20, blank=False)
    thumbnail = models.FileField(blank=True,null=True,upload_to=getUploadFileName)
    manufacturer = models.ForeignKey("Manufacturer", blank=True, null=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey("Supplier", blank=True, null=True, on_delete=models.SET_NULL)
    buyer = models.ManyToManyField("Buyer",  blank=True, null=True)
    price = models.IntegerField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    in_Stock = models.IntegerField(max_length=20, blank=True, null=True)
    source = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
            return self.shortName

    class Meta:
        abstract = True
        ordering = ['shortName']



class Weapon(Item):
    caliber = models.IntegerField(max_length=20, blank=True, null=True)
    keyFeature = models.CharField(max_length=100, blank=True, null=True)


class Misc(Item):
    type = models.CharField(max_length=50, blank=True)

class Ammo(Weapon):
    to = models.ForeignKey(Weapon, max_length=50, blank=True, related_name="ammunition")
    amount = models.IntegerField(max_length=20, blank=True, null=True)


class Person(models.Model):
    firstName = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField(max_length=20, blank=True, null= True)

    def __unicode__(self):
         return self.firstName


class Company(models.Model):
    shortName = models.CharField(max_length=20, blank=True)
    fullName = models.CharField(max_length=150, blank=False)
    country = models.CharField(max_length=50, blank=True)
    contact = models.ForeignKey(Person, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.fullName

class Manufacturer(Company):
    headquarters = models.CharField(max_length=50, blank=True)

class Buyer (Company):
    discount = models.IntegerField(max_length = 3, blank=True, null=True)

class Supplier(Company):
    pass


