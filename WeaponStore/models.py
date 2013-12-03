from django.db import models
# -*- coding: utf-8 -*-
class Item(models.Model):
    name = models.CharField(max_length=200, blank=False)
    caliber = models.IntegerField(max_length=20)
    year = models.IntegerField(max_length=4)
    desc = models.TextField(max_length=1000)
    manufacturer = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    in_Stock = models.IntegerField(max_length=20)

    class Meta:
        def __unicode__(self):
            return self.title



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