from . import views
from django.urls import path

urlpatterns=[
    path("/first",views.fun1)
]