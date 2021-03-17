from django.shortcuts import render
from .forms import RegistrationForm, RetrieveForm
# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            pass
    
    else:
        reg_form = RegistrationForm
        ret_form = RetrieveForm

    context = {'reg_form': reg_form, 'ret_form': ret_form}
    return render(request, 'MusicAppDB/index.html', context)

def retrieve(request):
    if request.method == 'POST':
        form = RetrieveForm(request.POST)
        if form.is_valid():
            pass
    
    else:
        reg_form = RegistrationForm
        ret_form = RetrieveForm

    context = {'reg_form': reg_form, 'ret_form': ret_form}
    return render(request, 'MusicAppDB/index.html', context)

def index(request):
    reg_form = RegistrationForm
    ret_form = RetrieveForm
    context = {'reg_form': reg_form, 'ret_form': ret_form}
    return render(request, 'MusicAppDB/index.html', context)