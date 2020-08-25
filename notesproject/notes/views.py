from django.shortcuts import render
from .models import Notes

# Create your views here.


def list_notes(request):
    notes = Notes.objects.all()
    return render(request, 'templates/list_notes.html', {'notes': notes})


def notes_detail(request):
    pass
