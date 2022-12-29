from django.urls import path
from .views import consumer_create,consumerEditView,StationeryCreate,StationeryEditView,ClothingCreate,ClothingEditView,Funriniturecreate,FunrinitureEditView,GroceryView,GroceryEditView,consumerprofileEdit
urlpatterns =[
    path('consumer/',(consumer_create.as_view())),
    path('consumeredit/<str:pk>',(consumerEditView.as_view())),
    path('gr/',(GroceryView.as_view())),
    path('gr_edit/<str:pk>',(GroceryEditView.as_view())),
    path('stcreate/',(StationeryCreate.as_view())),
    path('st_edit/<str:pk>',(StationeryEditView.as_view())),
    path('clcreate/',(ClothingCreate.as_view())),
    path('cl_edit/<str:pk>',(ClothingEditView.as_view())),
    path('funcreate/',(Funriniturecreate.as_view())),
    path('funedit/<str:pk>',(FunrinitureEditView.as_view())),
    path('consumerprofile_edit/<str:pk>',(consumerprofileEdit.as_view()))
]
