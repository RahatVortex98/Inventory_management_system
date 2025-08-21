from django.urls import path
from .views import *

urlpatterns =[

    path('inventory/',inventory,name="inventory"),
    path('product/<int:pk>',product,name='product'),
    

]