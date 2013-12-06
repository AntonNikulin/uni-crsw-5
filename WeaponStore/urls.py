from django.conf.urls import patterns, include, url
from WeaponStore import views

urlpatterns = patterns('',
                       url(r'^$', 'WeaponStore.views.Index', name='index'),
                       # Weapon CRUD
                       url(r'^l$', views.WeaponList.as_view(), name='weapon_list'),
                       url(r'^new$', views.WeaponCreate.as_view(success_url="/"), name='weapon_new'),
                       url(r'^edit/(?P<pk>\d+)$$', views.WeaponUpdate.as_view(success_url="/"), name='weapon_edit'),
                       url(r'^delete/(?P<pk>\d+)$$', views.WeaponDelete.as_view(success_url="/"), name='weapon_delete'),

)
