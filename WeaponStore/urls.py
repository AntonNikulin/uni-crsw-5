from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url (r'^$', 'WeaponStore.views.Index', name='index'),
        # Weapon CRUD
        url (r'^createweapon/$', 'WeaponStore.views.createWeapon', name='createWeapon'),
        url (r'^editweapon/(?P<id>\d+)$', 'WeaponStore.views.editWeapon', name='editWeapon'),
        url (r'^deleteweapon/(?P<id>\d+)$', 'WeaponStore.views.deleteWeapon', name='deleteWeapon'),
)
