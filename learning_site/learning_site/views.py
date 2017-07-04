from django.shortcuts import render
from . import forms


def hello_world(request):
    return render(request, 'home.html')

def suggestion_view(request):
    form = forms.SuggestionForm()  #instantiated a copy of our form
    return render(request, 'suggestion_form.html', {'form': form})