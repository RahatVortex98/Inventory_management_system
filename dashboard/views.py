from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import AddInventory,UpdateInventory
from django.contrib import messages

from django_pandas.io import read_frame
import plotly
import plotly.express as px
import json



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

def add_product(request):
    if request.method == "POST":
        add_form = AddInventory(request.POST)  # Bind form with POST data
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            # Calculate sales before saving
            new_inventory.sales = (
                float(add_form.cleaned_data['cost_per_item']) *
                float(add_form.cleaned_data['quantity_sold'])
            )
            new_inventory.save()
            return redirect('inventory')  # Redirect after successful save
    else:
        add_form = AddInventory()  # Empty form for GET request

    return render(request, 'inventory_add.html', {"form": add_form})

def remove_product(request,pk):
    inventory=get_object_or_404(Inventory,pk=pk)
    inventory.delete()
    messages.success(request, "Product removed successfully!")
    return redirect('inventory')

def update_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)

    if request.method == 'POST':
        updateForm = UpdateInventory(request.POST, instance=inventory)
        if updateForm.is_valid():
            updated_inventory = updateForm.save(commit=False)
            updated_inventory.sales = float(updated_inventory.cost_per_item) * float(updated_inventory.quantity_sold)
            updated_inventory.save()
            return redirect('inventory')  # use your correct URL name
    else:
        updateForm = UpdateInventory(instance=inventory)

    return render(request, 'inventory_update.html', {"form": updateForm})





def dashboard(request):
    inventories = Inventory.objects.all()
    df = read_frame(inventories)

    # 1. Sales Trend
    sales_graph = df.groupby(by='last_sales_date', as_index=False)['sales'].sum()
    sales_graph = px.line(sales_graph, x='last_sales_date', y='sales', title="Sales Trend")
    sales_graph = json.dumps(sales_graph, cls=plotly.utils.PlotlyJSONEncoder)

    # 2. Most Product in Stock
    most_product_in_stock_df = df[['name', 'quantity_in_stock']].sort_values(by='quantity_in_stock', ascending=False)
    stock_graph = px.bar(most_product_in_stock_df, x='name', y='quantity_in_stock', title="Most Product in Stock")
    stock_graph = json.dumps(stock_graph, cls=plotly.utils.PlotlyJSONEncoder)

    # 3. Best Performing Product (based on total sales)
    best_product_df = df.groupby('name', as_index=False)['sales'].sum().sort_values(by='sales', ascending=False)
    best_product_graph = px.bar(best_product_df, x='name', y='sales', title="Best Performing Products")
    best_product_graph = json.dumps(best_product_graph, cls=plotly.utils.PlotlyJSONEncoder)

    context = {
        'sales_graph': sales_graph,
        'stock_graph': stock_graph,
        'best_product_graph': best_product_graph,
    }
    return render(request, 'dashboard.html', context)