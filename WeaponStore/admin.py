from django.contrib import admin

from WeaponStore.models import Weapon, Manufacturer, Ammo, Buyer, Supplier, Person, Misc


admin.site.register(Weapon)
admin.site.register(Manufacturer)
admin.site.register(Ammo)
admin.site.register(Buyer)
admin.site.register(Supplier)
admin.site.register(Person)
admin.site.register(Misc)
