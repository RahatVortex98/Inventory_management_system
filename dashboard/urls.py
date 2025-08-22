from django.urls import path
from .views import *

urlpatterns =[

    path('inventory/',inventory,name="inventory"),
    path('product/<int:pk>',product,name='product'),
    path('product_add/',add_product,name='add_product'),
    path('product_remove/<int:pk>',remove_product,name='remove'),
    
    path('product_update/<int:pk>',update_product,name='update'),
    path('dashboard/',dashboard,name='dashboard'),
    

]