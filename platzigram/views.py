"""Platzigram views"""
#Estas son las "local_views"

# Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json


def current_time(request):
    """Return current time of server"""
    server_time = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse('Hello, current server time is {now}'.format(
    now=server_time
    ))


def say_hi(request, name, age):
    """Return greeting"""
    print(request)

    if age < 12:
        message = 'Sorry {name}, you don\'t have the permissions to access.'.format(
        name=name)
    else:
        message = 'Hello {name}, welcome to Platzigram.'.format(name=name)
    #este paquete es un debugger que permite consultar variables a
    #request en linea de comandos sin necesidad de estar imprimiendo y
    #actualizando en el navegador
    #import pdb;pdb.set_trace() # el ; es para no incluir el salto de linea

    return HttpResponse(message)


def sorted_numbers(request):
    """Return the sorted numbers typed by user on url"""
    numbers = request.GET['numbers']
    sorted_integers = sorted([int(i) for i in numbers.split(',')])
    data = {
        'status':'ok',
        'numbers':sorted_integers,
        'message': 'Integers sorted succesfully'
    }

    #import pdb;pdb.set_trace()
    return HttpResponse(json.dumps(data, indent=4),
    content_type='application/json'
    )
