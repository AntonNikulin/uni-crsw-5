from  django.shortcuts import render, get_object_or_404
from .models import Item


def Index(request):
    items = Item.objects.all()
    return render(request,'WeaponStore/index.html',{'items': items})