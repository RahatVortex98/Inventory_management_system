from django.forms import ModelForm
from .models import Inventory
from django import forms

class AddInventory(ModelForm):
    class Meta:
        model=Inventory
        fields = ['name','cost_per_item','quantity_in_stock','quantity_sold']


class UpdateInventory(ModelForm):
    class Meta:
        model=Inventory
        fields = ['name','cost_per_item','quantity_in_stock','quantity_sold']
        # Optional: disable sales so it shows but cannot be edited
        widgets = {
            'sales': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }