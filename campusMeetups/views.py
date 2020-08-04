import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import createMeetup


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "campusMeetups/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "campusMeetups/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        firstName = request.POST["fName"]
        lastName = request.POST["lName"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "campusMeetups/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                first_name=firstName, last_name=lastName, username=email, email=email, password=password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "campusMeetups/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "campusMeetups/register.html")

@csrf_exempt
def index(request):
         form = createMeetup(request.POST or None)
         if form.is_valid():
             obj = form.save(commit=False)
             obj.meetupCreator = User.objects.get(id=request.user.id)
             obj.save()
         return render(request, "campusMeetups/index.html", {
             'form': form
             })


@csrf_exempt
def enrollUser(request):
    if request.method == "POST":
        getMeetupId=request.POST["meetupID"]
        meetupObj = Meetups.objects.get(id = getMeetupId)
        meetupObj.signUp.add(User.objects.get(id=request.user.id))
        return HttpResponseRedirect(reverse("index"))

# Return Json
def meetups(request):
    if request.user.is_authenticated:
         # fetch all active meetups
        activeMeetups = Meetups.objects.filter(isActive=True)
        activeMeetups.order_by("-timestamp").all()
        return JsonResponse([meetups.serialize() for meetups in activeMeetups], safe=False)
    else:
        return HttpResponseRedirect(reverse("login"))

# Return Json
def enrolled(request):
    if request.user.is_authenticated:
         # fetch all meetups only user is enrolled in
        enrolledMeetups = User.objects.get(id=request.user.id).usersEnrolled.all()
        enrolledMeetups.order_by("-timestamp").all()
        return JsonResponse([enrolled.serialize() for enrolled in enrolledMeetups], safe=False)
    else:
        return HttpResponseRedirect(reverse("login"))


# Return Json
def profile(request):
    if request.user.is_authenticated:
        # fetch the user's profile info to JS
       user = User.objects.get(id = request.user.id)
       return JsonResponse([user.serialize()], safe=False)
    else:
        return HttpResponseRedirect(reverse("login"))


