from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import *
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import AboutInfo, Dish, ContactsInfo, FeedbackInfo
from .forms import AboutForm, UserLoginForm, FeedbackForm
from django.views.generic import UpdateView


class Index(View):
    def get(self, request):
        contacts = ContactsInfo.objects.all()
        feedback = FeedbackInfo.objects.all()
        return render(request, 'main/index.html', locals())

    def feedback_create(request):
        error = ''
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                error = 'Неверная форма заполнения'
        form = FeedbackForm()
        data = {
            'form': form,
            'error': error
        }
        return render(request, 'main/create_feedback.html', data)


def about(request):
    contacts = ContactsInfo.objects.all()
    abouts = AboutInfo.objects.all()
    return render(request, 'main/about.html', locals())


def menu(request):
    contacts = ContactsInfo.objects.all()

    return render(request, 'main/menu.html', {"contacts": contacts})


def contact(request):
    contacts = ContactsInfo.objects.all()
    return render(request, 'main/contact.html', {"contacts": contacts})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = User.objects.get(email=form.cleaned_data['email'])
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))
            else:
                error = 'Invalid username or password.'


class RegFormView(FormView):
    form_class = UserCreationForm
    success_url = '../login'
    template_name = 'main/registration.html'

    def form_valid(self, form):
        new_user = form.save()
        new_user.groups.add(Group.objects.get(name='users'))
        new_user.save()
        return super(RegFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegFormView, self).form_invalid(form)


class LogoutFormView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("../")


class AboutUpdateView(UpdateView):
    model = AboutInfo
    template_name = 'create_about.html'
    form_class = AboutForm


def create_about(request):
    error = ''
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма заполнения'
    form = AboutForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_about.html', data)


class DishView(View):
    def get(self, request):
        dishes = Dish.objects.all()
        return render(request, 'main/menu.html', {"dishes": dishes})


