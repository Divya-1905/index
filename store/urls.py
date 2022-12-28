from django.urls import path
from .views import GroceryView,GroceryEditView,consumer_create,consumerEditView,StatenoeryCreate,StatenoeryEditView,ClothingCreate,ClothingEditView,Funriniturecreate,FunrinitureEditView
urlpatterns =[
    path('consumer/',(consumer_create.as_view())),
    path('consumeredit/<str:pk>',(consumerEditView.as_view())),
    path('gr/',(GroceryView.as_view())),
    path('gredit/<str:pk>',(GroceryEditView.as_view())),
    path('statenoerycreate/',(StatenoeryCreate.as_view())),
    path('statenoeryedit/',(StatenoeryEditView.as_view())),
    path('clothingcreate/',(ClothingCreate.as_view())),
    path('clothingedit/',(ClothingEditView.as_view())),
    path('funriniturecreate/',(Funriniturecreate.as_view())),
    path('funrinitureedit/',(FunrinitureEditView.as_view())),
]
