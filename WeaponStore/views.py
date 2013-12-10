from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Weapon, Manufacturer, Buyer



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
    return render(request, 'WeaponStore/weapon_list.html', {'object_list': weapons})

def buyerItemList(request, id):
    buyers = Buyer.objects.get(pk=id)
    items = buyers.weapon_set.all()
    return render(request, 'WeaponStore/weapon_list.html', {'object_list': items})


#   Weapon CRUD
class WeaponList(ListView):
    model=Weapon

class WeaponCreate(CreateView):
    model = Weapon
    template_name = "WeaponStore/generic/generic_form.html"

class WeaponUpdate(UpdateView):
    model = Weapon
    template_name = "WeaponStore/generic/generic_form.html"

class WeaponDelete(DeleteView):
    model = Weapon

#   Manufacturer CRUD
class ManufacturerList(ListView):
    model = Manufacturer

class ManufacturerCreate(CreateView):
    model = Manufacturer
    template_name = "WeaponStore/generic/generic_form.html"

class ManufacturerUpdate(UpdateView):
    model = Manufacturer
    template_name = "WeaponStore/generic/generic_form.html"

class ManufacturerDelete(DeleteView):
    model = Manufacturer

#   Buyer CRUD
class BuyerList(ListView):
    model = Buyer

class BuyerCreate(CreateView):
    model = Buyer
    template_name = "WeaponStore/generic/generic_form.html"

class BuyerUpdate(UpdateView):
    model = Buyer
    template_name = "WeaponStore/generic/generic_form.html"

class BuyerDelete(DeleteView):
    model = Buyer