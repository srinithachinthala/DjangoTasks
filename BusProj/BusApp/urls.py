from django.urls import path
from . import views
urlpatterns=[
    path('',views.BusViews1,name="baseview"),
    path('del/<int:id>/',views.delete_data,name='deletedata'),
    path('<int:id>',views.update_data,name='update')
]