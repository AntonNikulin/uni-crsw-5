from django.db import models
# -*- coding: utf-8 -*-


class Item(models.Model):
    fullName = models.CharField(max_length=200, blank=True)
    shortName = models.CharField(max_length=20, blank=False)
    year = models.IntegerField(max_length=4, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    manufacturer = models.ForeignKey("Manufacturer", blank=True, null=True, on_delete=models.SET_NULL)
    country = models.CharField(max_length=50, blank=True, null=True)
    in_Stock = models.IntegerField(max_length=20, blank=True, null=True)
    source = models.URLField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['shortName']

        def __unicode__(self):
            return self.name


class Weapon(Item):
    caliber = models.IntegerField(max_length=20, blank=True, null=True)
    keyFeature = models.CharField(max_length=100, blank=True, null=True)


class Misc(Item):
    type = models.CharField(max_length=50, blank=True)


class Person(models.Model):
    firstName = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField(max_length=20, blank=True, null= True)

    class Meta:
        def __unicode__(self):
            return self.lastName


class Company(models.Model):
    shortName = models.CharField(max_length=20, blank=True)
    fullName = models.CharField(max_length=150, blank=False)
    country = models.CharField(max_length=50, blank=True)
    contact = models.ForeignKey(Person, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        def __unicode__(self):
            return self.shortName

class Manufacturer(Company):
    headquarters = models.CharField(max_length=50, blank=True)

class Buyer (Company):
    pass


