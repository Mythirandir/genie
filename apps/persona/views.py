from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth import logout
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            return redirect("persona:persona_admin")
        else:
            for message in form.error_messages:
                print(form.error_messages[message])

    form = NewUserForm
    return render(request,
                  "persona/sign_up.html",
                  context={"form": form})


# Log In
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("persona_admin")
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")
    form = AuthenticationForm()
    return render(request,
                  "persona/login.html",
                  {"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out Successfully!")
    return redirect("frontpage")


@login_required
def persona(request):
    return render(request=request,
                  template_name="persona/persona_admin.html",
                  )


@login_required
def event(request):
    events = Event.objects.all()

    return render(request, 'persona/events.html', {'events': events})


# @login_required
class AddEvents(CreateView):
    model = Event
    fields = [
        'event_creator',
        'event_name',
        'event_description',
        'event_location',
        'event_type',
        'event_date',
        'event_cart',
    ]
    template_name = 'persona/add_event.html'
    success_url = 'event_list'


class EventList(ListView):
    model = Event
    fields = [
        User,
        'event_name',
        'event_description',
        'event_location',
        'event_type',
        'event_date',
        'event_cart',
    ]
    template_name = 'persona/event_list.html'


