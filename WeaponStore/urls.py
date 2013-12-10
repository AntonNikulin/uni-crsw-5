from django.conf.urls import patterns, include, url
from WeaponStore import views

urlpatterns = patterns('',
    url(r'^$', 'WeaponStore.views.Index', name='index'),
    url(r'^search$', 'WeaponStore.views.search', name='search'),
    url(r'^manufactureritemlist/(?P<id>\d+)$','WeaponStore.views.manufacturerItemList', name='manufacturerItemList'),

    # Weapon CRUD
    url(r'^weapon/list$', views.WeaponList.as_view(), name='weapon_list'),
    url(r'^weapon/create$', views.WeaponCreate.as_view(success_url="/"), name='weapon_create'),
    url(r'^weapon/edit/(?P<pk>\d+)$', views.WeaponUpdate.as_view(success_url="/weapon/list"), name='weapon_edit'),
    url(r'^weapon/delete/(?P<pk>\d+)$', views.WeaponDelete.as_view(success_url="/weapon/list"), name='weapon_delete'),

    #Manufacturer CRUD
    url(r'^manufacturer/list$', views.ManufacturerList.as_view(), name='manufacturer_list'),
    url(r'^manufacturer/create$', views.ManufacturerCreate.as_view(success_url="/"), name='manufacturer_create'),
    url(r'^manufacturer/edit/(?P<pk>\d+)$', views.ManufacturerUpdate.as_view(success_url="/manufacturer/list"), name='manufacturer_edit'),
    url(r'^manufacturer/delete/(?P<pk>\d+)$', views.ManufacturerDelete.as_view(success_url="/manufacturer/list"), name='manufacturer_delete'),

    #Buyer CRUD
    url(r'^Buyer/list$', views.BuyerList.as_view(), name='buyer_list'),
    url(r'^Buyer/create$', views.BuyerCreate.as_view(success_url="/"), name='buyer_create'),
    url(r'^Buyer/edit/(?P<pk>\d+)$', views.BuyerUpdate.as_view(success_url="/buyer/list"), name='buyer_edit'),
    url(r'^Buyer/delete/(?P<pk>\d+)$', views.BuyerDelete.as_view(success_url="/buyer/list"), name='buyer_delete'),


)
