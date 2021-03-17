from django.shortcuts import render
from .forms import RegistrationForm, RetrieveForm
from .models import Users, ArtistAttributes, Artists, Ratings
# Create your views here.

def registration(request):
    reg_form = RegistrationForm
    ret_form = RetrieveForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            context = {'reg_form': reg_form, 'ret_form': ret_form}
    
    else:
        context = {'reg_form': reg_form, 'ret_form': ret_form}

    return render(request, 'MusicAppDB/index.html', context)

def songret(request):
    reg_form = RegistrationForm
    ret_form = RetrieveForm
    if request.method == 'POST':
        form = RetrieveForm(request.POST)
        if form.is_valid():
            ratings = Ratings.objects.all()
            context = {'reg_form': reg_form, 'ret_form': ret_form, 'ratings': ratings}
    
    else:
        context = {'reg_form': reg_form, 'ret_form': ret_form}
    
    return render(request, 'MusicAppDB/index.html', context)

def artistret(request):
    reg_form = RegistrationForm
    ret_form = RetrieveForm
    if request.method == 'POST':
        form = RetrieveForm(request.POST)
        if form.is_valid():
            pass
    
    else:
        pass

    context = {'reg_form': reg_form, 'ret_form': ret_form}
    return render(request, 'MusicAppDB/index.html', context)

def index(request):
    reg_form = RegistrationForm
    ret_form = RetrieveForm
    context = {'reg_form': reg_form, 'ret_form': ret_form}
    return render(request, 'MusicAppDB/index.html', context)