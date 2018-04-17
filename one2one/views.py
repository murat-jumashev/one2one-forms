from django.shortcuts import render
from .forms import UserForm


def index(request):
    context = {
        'form': UserForm()
    }
    return render(request, 'one2one/index.html', context)
