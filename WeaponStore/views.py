from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Weapon, Manufacturer



def Index(request):
    items = Weapon.objects.all()
    return render(request, 'WeaponStore/index.html', {'weapon': items})

def search(request):
    if 'queryWeapon' in request.GET:
        weapon = Weapon.objects.filter(shortName__contains = request.GET['queryWeapon'])
        return render(request, 'WeaponStore/Search.html', {'weapon': weapon})

def manufacturerItemList(request, id):
    manufacturer = Manufacturer.objects.get(pk=id)
    weapons = manufacturer.weapon_set.all()
    return (request, 'WeaponStore/weapon_list.html', {'object_list': weapons})


#   Weapon CRUD
class WeaponList(ListView):
    model=Weapon

class WeaponCreate(CreateView):
    model=Weapon

class WeaponUpdate(UpdateView):
    model = Weapon

class WeaponDelete(DeleteView):
    model = Weapon

#   Manufacturer CRUD
class ManufacturerList(ListView):
    model = Manufacturer

class ManufacturerCreate(CreateView):
    model = Manufacturer

class ManufacturerUpdate(UpdateView):
    model = Manufacturer

class ManufacturerDelete(DeleteView):
    model = Manufacturer