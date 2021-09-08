from django.urls import path
from  . import views

urlpatterns=[
path('',views.index),
path('add',views.add),
path('ShowC',views.ShowClASS),
path('ShowT',views.ShowTeacher),
path('api',views.api),
path('insert',views.ADDapi)

]