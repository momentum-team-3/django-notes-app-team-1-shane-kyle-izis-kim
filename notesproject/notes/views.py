from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.


def list_notes(request):
    notes = Note.objects.all()
    return render(request, 'list_notes.html', {'notes': notes})


def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'notes_detail.html', {'note': note})


def add_note(request):
    if request.method == "GET":
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_notes')
    return render(request, 'add_note.html', {'form': form})