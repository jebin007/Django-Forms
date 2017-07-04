from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from . import forms


def hello_world(request):
    return render(request, 'home.html')

def suggestion_view(request):
    form = forms.SuggestionForm()  #instantiated a copy of our form
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST) #fills in the data from the request
        if form.is_valid():
            send_mail(
                'Suggestion from {}'.format(form.cleaned_data['name']),#from
                form.cleaned_data['suggestion'],#suggestion
                '{name} <{email}>'.format(**form.cleaned_data),#emailfrom
                ['jevinsubedi@gmail.com']
            )
            messages.add_message(request, messages.SUCCESS, 'Thanks for your suggestion!')
            return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'suggestion_form.html', {'form': form})