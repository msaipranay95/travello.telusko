from  django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    #path('add', views.add, name='add'),  #should not put slash(/) in this line for further exicution....
]
