from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Weapon
from .forms import WeaponForm


def Index(request):
    items = Weapon.objects.all()
    return render(request, 'WeaponStore/index.html', {'items': items})


def createWeapon(request):
    if request.POST:
        form = WeaponForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'WeaponStore/WeaponForm.html', {'form': form})
    else:
        form = WeaponForm()
        return render(request, 'WeaponStore/WeaponForm.html', {'form': form})

def editWeapon(request, id):
    object = get_object_or_404(Weapon, pk=id)
    form = WeaponForm(instance=object)
    return render(request, 'WeaponStore/WeaponForm.html', {'form': form})

def deleteWeapon(request, id):
    pass