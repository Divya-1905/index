from django.urls import path
from .views import GroceryView,GroceryEditView,consumer_create,consumerEditView
urlpatterns =[
    path('consumer/',(consumer_create.as_view())),
    path('consumeredit/<str:pk>',(consumerEditView.as_view())),
    path('gr/',(GroceryView.as_view())),
    path('gredit/<str:pk>',(GroceryEditView.as_view())),
]
