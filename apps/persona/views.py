from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.contrib.auth import logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from apps.product.models import Product
from apps.cart.cart import Cart


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
    events = Event.objects.all()
    return render(request, "persona/persona_admin.html", {'events': events})


@login_required
def add_events(request):
    newest_products = Product.objects.all()[0:8]
    cart = Cart

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('persona_admin')
    else:
        form = EventForm()

    return render(request, 'persona/add_event.html', {'form': form, 'newest_products': newest_products, 'cart': cart})


@login_required
def view_event(request, pk):
    event = get_object_or_404(Event, id=pk)
    return render(request, 'persona/event_detail.html', {'event': event})


@login_required
def update_event(request, pk):
    event = get_object_or_404(Event, id=pk)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('persona_admin')
    return render(request, 'persona/update_event.html', {'form': form})


@login_required
def delete_event(request, pk):
    context = {}
    event = get_object_or_404(Event, id=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('persona_admin')
    return render(request, 'persona/delete_event.html', context)
