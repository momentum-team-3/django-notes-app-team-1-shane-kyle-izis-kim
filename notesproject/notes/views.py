from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('list_notes')
    return render(request, 'add_note.html', {'form': form})


# # def edit_note(request, pk):
#     note = Note.objects.get(pk=pk)
#     if request.method == "GET":
#         form = NoteForm(instance=note)
#     else:
#         form = NoteForm(data=request.POST, instance=note)
#         if form.is_valid():
#             form.save()
#             return redirect('list_notes')
#     return render(request, 'edit_note.html', {'note': note})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "GET":
        form = NoteForm(instance=note)
    else:
        form = NoteForm(data=request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('list_notes')
    return render(request, 'edit_note.html', {
        'form': form,
        'note': note
    })
