from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Weapon
from .forms import WeaponForm



def Index(request):
    items = Weapon.objects.all()
    return render(request, 'WeaponStore/index.html', {'weapon': items})

def search(request):
    if 'queryWeapon' in request.GET:
        weapon = Weapon.objects.filter(shortName__contains = request.GET['queryWeapon'])
        return render(request, 'WeaponStore/Search.html', {'weapon': weapon})


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