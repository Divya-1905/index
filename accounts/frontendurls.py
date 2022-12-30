from django.urls import path
from .frontendviews import Signup,Login

urlpatterns =[
       path('signup/',Signup),
       path('login/',Login),
]