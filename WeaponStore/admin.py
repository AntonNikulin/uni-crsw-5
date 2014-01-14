from django.contrib import admin

from WeaponStore.models import Weapon, Manufacturer, Person, Misc


admin.site.register(Weapon)
admin.site.register(Manufacturer)
admin.site.register(Person)
admin.site.register(Misc)
