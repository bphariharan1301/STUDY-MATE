from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from base.models import Room
from .forms import *

# Create your views here.


def home(request):
    rooms = Room.objects.all().order_by('-updated', '-created')

    context = {
        'rooms': rooms,
    }

    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)

    context = {
        'room': room,
    }

    return render(request, 'base/room.html', context)


def create_room(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'base/room_form.html', context)
