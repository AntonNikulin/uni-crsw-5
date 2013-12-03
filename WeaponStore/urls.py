from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url (r'^$', 'WeaponStore.views.Index', name='index'),
        url (r'^createItem/$', 'WeaponStore.views.createItem', name='createItem'),
)
