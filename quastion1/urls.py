from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('name',views.Name),
    path('fqus',views.Firstbranch),


]