from django.db import models
# -*- coding: utf-8 -*-
from time import time

def getUploadFileName(instance, filename):
    return "%s_%s" % (str(time()).replace('.','_'), str(filename))

clr = (
        (u'Нереально розовый ', u'Нереально розовый '),
        (u'Истинно зеленый ', u'Истинно зеленый '),
        (u'Цвет брюк Джентльманна ', u'Цвет брюк Джентльманна '),
        (u'Мускулисто-коричневый ', u'Мускулисто-коричневый '),
        (u'Странный оттенок серого ', u'Странный оттенок серого ')
    )

class Item(models.Model):
    fullName = models.CharField(max_length=200, blank=True)
    shortName = models.CharField(max_length=50, blank=False)
    thumbnail = models.FileField(blank=True,null=True,upload_to=getUploadFileName)
    manufacturer = models.ForeignKey("Manufacturer", blank=True, null=True, on_delete=models.SET_NULL)
    source = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    color = models.CharField(max_length=30,
                                        choices=clr,
                                        default=u'Повседневный', blank=True, null=True)
    def __unicode__(self):
            return self.shortName

    class Meta:
        abstract = True
        ordering = ['shortName']



class Weapon(Item):
    caliber = models.IntegerField(max_length=5, blank=True, null=True)
    addtInfo = models.CharField(max_length=200, blank=True, null=True)


class Misc(Item):
    type = models.CharField(max_length=50, blank=True)


class Person(models.Model):
    firstName = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField(max_length=20, blank=True, null= True)
    position = models.CharField(max_length=50, blank=True, null=True)

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
    pass




