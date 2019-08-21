from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'MATETI HOME'
    dest1.desc = 'ITS A FAMILY FAVIOURATE PLACE LOCATED IN THE HEART OF INDIA'
    dest1.img ='destination_1.jpg'
    dest1.price = 100
    dest1.offer= 'false'

    dest2 = Destination()
    dest2.name = 'KOTHAGUDEM'
    dest2.desc = 'ITS A LOCATION WHERE I GROW UP '
    dest2.img = 'destination_2.jpg'
    dest2.price = 200
    dest2.offer = 'false'

    dest3 = Destination()
    dest3.name = 'WARANAGAL'
    dest3.desc = 'ITS A LOCATION WHERE PAPA GROWNUP'
    dest3.img = 'destination_3.jpg'
    dest3.price = 300
    dest3.offer='false'

    dests=[dest1,dest2,dest3]

    return  render(request, "index.html",{'dests':dests})


