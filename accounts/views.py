from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Muvaffaqiyatli login amalga oshirildi')
                else:
                    return HttpResponse("Siz registratsiyadan o'tmagansiz")

            else:
                return HttpResponse("login yoki parolda xatolik bor")

    else:
        form = LoginForm()
        context = {
            'form': form
        }

    return render(request, 'registration/login.html', context)


def dashboard_view(request):
    user = request.user
    context = {
        'user': user
    }

    return render(request, 'pages/user_profile', context)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/register.html'
