from django.shortcuts import render
from .models import Note

# Create your views here.


def list_notes(request):
    notes = Note.objects.all()
    return render(request, 'list_notes.html', {'notes': notes})


def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'notes_detail.html', {'note': note})
