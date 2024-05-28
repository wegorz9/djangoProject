from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
from .models import Note


class NoteListView(ListView):
    model = Note
    template_name = 'note_list.html'


@login_required
def note_detail_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_detail.html', {'form': form})


def note_create_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_create.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signing up
            return redirect('note_list')  # Redirect to a successful registration page or another page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
