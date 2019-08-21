from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render( request, 'home.html',{'name':'pranay sonali'})

#"<h1>hi this is the home page</h1><br/>"
#                       "<h1>this is the 1st page i have created in this django i m so excite to execute more </h1>"
#                        "<input type='submit' >"


def add(request):
    val1 = int(request.POST['num1']) # here i should not add "" this double commas
    val2 = int(request.POST['num2'])
    res = val1+val2

    return render( request,'result.html',{'result':res})
