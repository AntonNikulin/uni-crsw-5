from django.db import models
# -*- coding: utf-8 -*-
class Item(models.Model):
    name = models.CharField(max_length=200, blank=False)
    caliber = models.IntegerField(max_length=20, blank=True, null=True )
    year = models.IntegerField(max_length=4, blank=True, null=True )
    desc = models.TextField(max_length=1000, blank=True, null=True )
    manufacturer = models.CharField(max_length=200, blank=True, null=True )
    country = models.CharField(max_length=50, blank=True, null=True )
    in_Stock = models.IntegerField(max_length=20, blank=True, null=True )

    class Meta:
        def __unicode__(self):
            return self.name



"""
# -*- coding: utf-8 -*-
#поставщик (foreign key to suppplyer)
    Мета: абстрактный?
        weapon, misc классы?



class #supplyer
    название
    адрес
    страна


class Покупатель
    название
    контактное лицо (ключ на персон)
    юр.адрес


class персон
    имя
    фамилия
    телефон
"""