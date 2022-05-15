from django.contrib.auth import authenticate, login
from django.shortcuts import render

from authentication.forms import LoginForm


def login_page(request):
    form = LoginForm()
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                message = f"Hello {user.email}! You have been logged in"
            else:
                message = "Login failed!"
    context = {"form": form, "message": message}
    return render(request, "login.html", context)
