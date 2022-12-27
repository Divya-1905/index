from django.urls import path
from .views import consumercreate,consumerEditView
urlpatterns =[
    path('consumer/',(consumercreate.as_view())),
    path('edit/',(consumerEditView.as_view())),
]
