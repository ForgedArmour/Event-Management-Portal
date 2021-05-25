from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import UserRegisterForm
from .models import makeEvent
from .forms import eventMakerForm
from mySite.models import myEvent

def index(request):
    user = request.user

    if user.is_authenticated:
        events = makeEvent.objects.all()
        params = {'event':events}
        return render(request, 'UserHome.html',params)
        
    else:
        return render(request, 'index.html')

def profile(request):
    user = request.user
    if user.is_authenticated:
        id = user.id
        username = user.username
        email = user.email
        if id==2:
            usertype = 'Coordinator'
        else:
            usertype = 'Normal User'
        return render(request,'profile.html',{'username':username,'email':email,'usertype':usertype})


def regevents(request):
    user = request.user
    username = user.username
    if user.is_authenticated:
        regevent = myEvent.objects.filter(myeve_username=username)
        return render(request,'registeredEvents.html',{'regevent':regevent})
    else:
        return HttpResponse('Go away Stranger')

def eventview(request, myid):
    event = makeEvent.objects.filter(id=myid)
    user = request.user
    if user.is_authenticated:
        username = request.user.username
        email = request.user.email
        eventname = event[0].event_name
        eventdesc = event[0].event_desc
        eventcontact = event[0].event_contact
        myevent = myEvent(myeve_name=eventname, myeve_username=username, myeve_email=email, myeve_desc=eventdesc, myeve_contact=eventcontact)
        myevent.save()
        
        return render(request,'Eventviewregister.html',{'event':event[0]})
    else:
        return HttpResponse('stranger')

def login(request):
    if request.method == 'POST':
        loginusername = request.POST['name']
        loginpassword = request.POST['pass']
        user = authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully Logged in !")
            return redirect('home')
        else:
            messages.success(request, "Invalid details. Please try again !")
            return redirect('home')
    else:
        return render(request,'login.html')



def logout(request):
    auth_logout(request)
    messages.success(request, "Successfully Logged out !")
    return redirect('home')

def about(request):
    return render(request, 'about.html')


def handleCreateEvent(request):
    user = request.user
    id = user.id
    print(user.id)
    if user.is_authenticated and id==2:
        return redirect('createEvent')
    else:
        return redirect('error')

def error(request):
    return render(request,'error.html',{'errormessage':'Only Coordinators can Access this page. Plz login with a coordinator Account'})

def createEvent(request):
    if request.method == 'POST':
        form=eventMakerForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            eventn = form.cleaned_data.get('event_name')
            print("vaild")
            form.save()
            messages.success(request, f'Event created for {eventn}!')
            return redirect('home')

    else:
        form=eventMakerForm()    
        return render(request,"createEvent.html",{"form":form})
        


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('vaild')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {"form":form})
 