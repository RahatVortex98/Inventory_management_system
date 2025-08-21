from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def inventory(request):
    inventories = Inventory.objects.all()

    context={
        'inventories':inventories
    }
    return render(request,'inventory.html',context=context)

@login_required
def product(request,pk):
    inventory=get_object_or_404(Inventory,pk=pk)

    context={
        'inventory':inventory
    }
    return render(request,'product.html',context=context)