from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
# Create your views here.
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

#def about(request):
    #return HttpResponse("Rango says here is the about page.<a href='/rango/'>index</a>")


def about(request):
    context_dict = {'boldmessage': "Welcome to the new exercise!"}
# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.
    return render(request, 'rango/about.html', context=context_dict)
