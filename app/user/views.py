# -*- coding: utf8 -*-
from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import UserForm, UserProfileForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/theory/')
        else:
            args['login_error'] = u"Пользователь не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/theory/')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return redirect('/user/login/')
        else:
            print(user_form.errors, profile_form.errors)
            return redirect('/user/register/')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})