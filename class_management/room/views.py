from email import message
from django.shortcuts import render
from room.models import *

# @login_required from contrib.auth.decorators 
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

def room(request, slug):
    room = Room.objects.get(slug=slug)
    message = Message.objects.filter(room=room)[0:4]

    return render(request, 'room.html', {'room': room, 'messages': message})


