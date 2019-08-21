from  django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),  #should not put slash in this line for further exicution....
]
