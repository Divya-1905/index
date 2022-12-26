from  django.urls import path
from.views import signupview,loginview
urlpatterns = [
    path('signup/',(signupview.as_view())),
    path('login/',(loginview.as_view())),
]
