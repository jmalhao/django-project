from django.urls import path

from . import views

#from django.urls import re_path
#from . import views

urlpatterns = [
    path('', views.main, name='main'),
    #path('', views.Django_First_App, name='Django_First_App'),
    #path('', views.index2, name="index2"),

    #re_path(r'^$', views.index2, name='index2'),
]