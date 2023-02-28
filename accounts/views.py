from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CustonLoginForm
from .admin import CustomUserCreationForm
from django.contrib import messages


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustonLoginForm


def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('login')

        else:
            print('invalid registration details')

    return render(request, "registration/register.html", {"form": form})


