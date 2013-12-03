from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Item
from .forms import ItemForm


def Index(request):
    items = Item.objects.all()
    return render(request, 'WeaponStore/index.html', {'items': items})

def createItem(request):
    if request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ItemForm()
        return render(request, 'WeaponStore/ItemForm.html', {'form': form})
