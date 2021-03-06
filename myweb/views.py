from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404
from .models import inputanime2


# Create your views here.
def index(req):
	#return HttpResponse(req.method)
    return render(req,'myweb/index.html')


def detail(request, question_id):
    return render(request, 'myweb/detail.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def Login(req):
    return render(req, 'myweb/Login.html')

def Logout(req):
    logout(req)
    return redirect("/")

def Register(req):
    return render(req, 'myweb/Register.html')

def anime(req):
    return render(req, 'myweb/anime.html')

def anime1(req):
    return render(req, 'myweb/anime1.html')

def anime2(req):
    inputanime2s = inputanime2.objects.all()
    return render(req, 'myweb/anime2.html', {'inputanime2s': inputanime2s})

def Register(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f"New account created: {username}")
            login(req, user)
            return redirect("/")

        else:
            for msg in form.error_messages:
                messages.error(req, f"{msg}: {form.error_messages[msg]}")

            return render(req,
                          template_name = "myweb/Register.html",
                          context={"form":form})
    form = UserCreationForm(req.POST)
    return render(req,
                template_name = "myweb/Register.html",
                context={"form":form})

def Login(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                messages.info(req, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(req, "Invalid username or password.")
        else:
            messages.error(req, "Invalid username or password.")
    form = AuthenticationForm()
    return render(req,
                  template_name = "myweb/Login.html",
                  context={"form":form})

def insertmovie(request):
    if request.method == 'POST':
        img = request.POST.get("img")
        animename = request.POST.get("animename")
        link = request.POST.get("link")
        add = inputanime2(img=img,animename=animename,link=link)
        add.save()
        return redirect('/anime2/')
    return render(request, 'myweb/insertmovie.html')

def insertmovies(req):
    inputanime2s = inputanime2.objects.all()
    ins = {
        'inputanime2s' : inputanime2s
        }
    return render(req, 'myweb/insertmovie.html', ins)
