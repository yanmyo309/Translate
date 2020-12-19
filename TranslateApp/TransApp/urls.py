from django.urls import path
from .views import Login,Translate


urlpatterns = [
    path('',Login,name='login'),
    path('/trans',Translate,name='trans')
]
