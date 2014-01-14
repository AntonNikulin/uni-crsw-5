from django.conf.urls import patterns, include, url
from WeaponStore import views

urlpatterns = patterns('',
    url(r'^$', 'WeaponStore.views.Index', name='index'),
    url(r'^search$', 'WeaponStore.views.search', name='search'),
    url(r'^manufactureritemlist/(?P<id>\d+)$','WeaponStore.views.manufacturerItemList', name='manufacturerItemList'),
    url(r'^buyeritemlist/(?P<id>\d+)$','WeaponStore.views.buyerItemList', name='buyerItemList'),

    # Weapon CRUD
    url(r'^weapon/list$', views.WeaponList.as_view(), name='weapon_list'),
    url(r'^weapon/create$', views.WeaponCreate.as_view(success_url="/"), name='weapon_create'),
    url(r'^weapon/edit/(?P<pk>\d+)$', views.WeaponUpdate.as_view(success_url="/weapon/list"), name='weapon_edit'),
    url(r'^weapon/detail/(?P<pk>\d+)$', views.WeaponDetail.as_view(), name='weapon_detail'),
    url(r'^weapon/delete/(?P<pk>\d+)$', views.WeaponDelete.as_view(success_url="/weapon/list"), name='weapon_delete'),

    #Manufacturer CRUD
    url(r'^manufacturer/list$', views.ManufacturerList.as_view(), name='manufacturer_list'),
    url(r'^manufacturer/create$', views.ManufacturerCreate.as_view(success_url="/"), name='manufacturer_create'),
    url(r'^manufacturer/edit/(?P<pk>\d+)$', views.ManufacturerUpdate.as_view(success_url="/manufacturer/list"), name='manufacturer_edit'),
    url(r'^manufacturer/delete/(?P<pk>\d+)$', views.ManufacturerDelete.as_view(success_url="/manufacturer/list"), name='manufacturer_delete'),

    #Misc CRUD
    url(r'^misc/list$', views.MiscList.as_view(), name='misc_list'),
    url(r'^misc/create$', views.MiscCreate.as_view(success_url="/"), name='misc_create'),
    url(r'^misc/edit/(?P<pk>\d+)$', views.MiscUpdate.as_view(success_url="/misc/list"), name='misc_edit'),
    url(r'^misc/detail/(?P<pk>\d+)$', views.MiscDetail.as_view(), name='misc_detail'),
    url(r'^misc/delete/(?P<pk>\d+)$', views.MiscDelete.as_view(success_url="/misc/list"), name='misc_delete'),


)
