from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Contact
from django.conf import settings
from .models import Document, Images
from .forms import DocumentForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
def index(request):
    return render(request, 'teyim/index.html')

def gallery(request):

    images = Images.objects.all()


    return render(request, 'teyim/gallery.html', {"images":images})

def gallery2(request):
    return render(request, 'teyim/gallery2.html')

def gallery3(request):
    return render(request, 'teyim/gallery3.html')

def street(request):
    return render(request, 'teyim/street.html')

def still(request):
    return render(request, 'teyim/still.html')

def nature(request):
    return render(request, 'teyim/nature.html')

def portrait(request):
    return render(request, 'teyim/portrait.html')

def about(request):
    return render(request, 'teyim/about.html')



@login_required(login_url="/teyim/login")
def contribute(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'teyim/contribute.html', {
        'form': form
    })


def contact(request):
    if request.method=="POST":
        contactt=Contact()
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contactt.fname=fname
        contactt.lname=lname
        contactt.email=email
        contactt.subject=subject
        contactt.message=message
        contactt.save()
        
        
        email_message = EmailMessage(
            subject = fname + " : " +subject,
            body = message,
            to = ['your email'],
            headers = {"Reply-To": email}
        )
        email_message.send()

    return render(request, 'teyim/contact.html')



User = get_user_model()


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "teyim/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "teyim/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "teyim/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "teyim/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "teyim/register.html")
